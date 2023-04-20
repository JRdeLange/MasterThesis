#https://stackoverflow.com/questions/54188353/how-do-i-make-3d-in-pyglet
#https://github.com/01AutoMonkey/open.gl-tutorials-to-pyglet
#https://towardsdatascience.com/beginners-guide-to-custom-environments-in-openai-s-gym-989371673952

import math
import random
import numpy as np
from scipy.spatial.transform import Rotation as R


class Utils:

    @staticmethod
    def capped_quaternion(forward, goal, max_theta):
        # check for slight inaccuracies (?) that cause an invalid arccos
        check = np.dot(goal, forward)
        if check > 1:
            check = 1
        if check < -1:
            check = -1
        theta = -np.arccos(check)
        if abs(theta) > max_theta:
            theta = math.copysign(max_theta, theta)
        # Find axis
        # Check if forward and goal aren't (anti)parallel
        axis = np.cross(goal, forward)
        if Utils.has_zeroes(axis):
            # If they are (anti)parallel, move the goal a tiny tiny bit
            goal = Utils.normalize([goal[0] + 0.01, goal[1], goal[2] + 0.01])
            axis = np.cross(goal, forward)
            if Utils.has_zeroes(axis):
                # If they are (anti)parallel, move the goal a tiny tiny bit
                goal = Utils.normalize([goal[0], goal[1] + 0.01, goal[2] + 0.01])
                axis = np.cross(goal, forward)

        axis = Utils.normalize_nparray(axis)
        # Construct quaternion
        quaternion = Utils.construct_quaternion(axis[0], axis[1], axis[2], theta)
        '''if not np.isfinite(quaternion):
            print(1, quaternion, axis, theta, forward, goal)'''
        try:
            np.asarray_chkfinite(quaternion)
        except ValueError:
            #<class 'ValueError'> [nan, nan, nan, 0.9995065603657316] [nan nan nan] -0.06283185307179587 [-0.57735027 -0.57735027 -0.57735027] [0.5773502691896258, 0.5773502691896258, 0.5773502691896258]
            print(ValueError, quaternion, axis, theta, forward, goal)

        return quaternion

    @staticmethod
    def has_zeroes(thing):
        for number in thing:
            if number != 0:
                return False
        return True

    @staticmethod
    def construct_quaternion(x, y, z, t):
        return [np.sin(t / 2) * x, np.sin(t / 2) * y, np.sin(t / 2) * z, np.cos(t / 2)]

    @staticmethod
    def wrapping_distance_vector(origin, to):
        vec = [0, 0, 0]
        # Construct all options
        x_options = [to[0] - 2, to[0], to[0] + 2]
        y_options = [to[1] - 2, to[1], to[1] + 2]
        z_options = [to[2] - 2, to[2], to[2] + 2]
        # Construct vector
        vec[0] = Utils.best_option(origin[0], x_options)
        vec[1] = Utils.best_option(origin[1], y_options)
        vec[2] = Utils.best_option(origin[2], z_options)
        return vec

    # Select lowest distance option
    @staticmethod
    def best_option(origin, options):
        lowest = 10
        raw_dist = None
        # Find the closest option
        for option, value in enumerate(options):
            dist = value - origin
            if abs(dist) < lowest:
                lowest = abs(dist)
                raw_dist = dist
        # Return the distance
        return raw_dist

    @staticmethod
    def vec3_magnitude(vec):
        return np.sqrt(vec[0]*vec[0] + vec[1]*vec[1] + vec[2]*vec[2])

    @staticmethod
    def world_to_unit(world, x, y, z):
        dim_x, dim_y, dim_z = world.get_size()
        x = x / dim_x * 2 - 1
        y = y / dim_y * 2 - 1
        z = z / dim_z * 2 - 1
        return x, y, z

    @staticmethod
    def world_to_render_spot(world, x, y, z):
        dim_x, dim_y, dim_z = world.get_size()
        x = (x-dim_x/2) / dim_x
        y = (y-dim_y/2) / dim_y
        z = (z-dim_z/2) / dim_z
        return x, y, z - 1.7

    @staticmethod
    def world_to_pixels(renderer, world, x, y):
        win_x, win_y = renderer.window.get_size()
        dim_x, dim_y = world.get_size()
        x = x / dim_x * win_x
        y = y / dim_y * win_y
        return x, y

    @staticmethod
    def radians_to_vec(r):
        return math.sin(r), math.cos(r)

    @staticmethod
    def get_direction_vec(x, y, z):
        pass

    @staticmethod
    def normalize(vec):
        scalar = 0
        for element in vec:
            scalar += element*element
        scalar = math.sqrt(scalar)
        newvec = []
        for element in vec:
            newvec.append(element / scalar)
        return newvec

    @staticmethod
    def normalize_nparray(arr):
        scalar = 0
        for element in arr:
            scalar += element * element
        scalar = math.sqrt(scalar)
        if scalar == 0:
            print("Changed a vector by +[0.01, 0.01, 0.01] to prevent division by zero in normalization")
            return Utils.normalize_nparray(arr + 0.01)
        return arr / scalar

    @staticmethod
    def perspective(aspect, fov, near, far):
        return ((1/(aspect*math.tan(fov/2)),0,0,0),
                (0,1/math.tan(fov/2),0,0),
                (0,0,(near+far)/(near-far),(2*near*far)/(near-far)),
                (0,0,-1,0))

    @staticmethod
    def scale(x=1, y=1, z=1):
        return ((float(x), 0., 0., 0.),
                (0., float(y), 0., 0.),
                (0., 0., float(z), 0.),
                (0., 0., 0., 1.))

    @staticmethod
    def translate(x=0, y=0, z=0):
        return ((1., 0., 0., float(x)),
                (0., 1., 0., float(y)),
                (0., 0., 1., float(z)),
                (0., 0., 0., 1.))

    @staticmethod
    def rotate(x=0, y=0, z=0):
        mat_x = ((1., 0., 0., 0.),
                 (0., math.cos(x), -math.sin(x), 0.),
                 (0., math.sin(x), math.cos(x), 0.),
                 (0., 0., 0., 1.))

        mat_y = ((math.cos(y), 0., -math.sin(y), 0.),
                 (0., 1., 0., 0.),
                 (math.sin(y), 0., math.cos(y), 0.),
                 (0., 0., 0., 1.))

        mat_z = ((math.cos(z), -math.sin(z), 0., 0.),
                 (math.sin(z), math.cos(z), 0., 0.),
                 (0., 0., 1., 0.),
                 (0., 0., 0., 1.))

        return np.dot(mat_x, np.dot(mat_y, mat_z))

    @staticmethod
    def identity():
        return ((1., 0., 0., 0.),
                (0., 1., 0., 0.),
                (0., 0., 1., 0.),
                (0., 0., 0., 1.))

    @staticmethod
    def combine_matrices(trans, scale, rot):
        return np.dot(trans, np.dot(rot, scale))


    @staticmethod
    def random_np_array(n, min, max):
        range = abs(max - min)
        l = np.random.rand(n) * range + min
        return l


