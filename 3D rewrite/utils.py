#https://stackoverflow.com/questions/54188353/how-do-i-make-3d-in-pyglet
#https://github.com/01AutoMonkey/open.gl-tutorials-to-pyglet
#https://towardsdatascience.com/beginners-guide-to-custom-environments-in-openai-s-gym-989371673952

import math
import random
import numpy as np
from scipy.spatial.transform import Rotation as R


class Utils:

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


