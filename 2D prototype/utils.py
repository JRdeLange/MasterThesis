#https://stackoverflow.com/questions/54188353/how-do-i-make-3d-in-pyglet
#https://github.com/01AutoMonkey/open.gl-tutorials-to-pyglet
#https://towardsdatascience.com/beginners-guide-to-custom-environments-in-openai-s-gym-989371673952

import math
import numpy as np


class Utils:

    @staticmethod
    def world_to_screen(world, x, y):
        dim_x, dim_y = world.get_size()
        x = x / dim_x * 2 - 1
        y = y / dim_y * 2 - 1
        return x, y

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

        return np.dot(mat_z, np.dot(mat_y, mat_x))

    @staticmethod
    def identity():
        return ((1., 0., 0., 0.),
                (0., 1., 0., 0.),
                (0., 0., 1., 0.),
                (0., 0., 0., 1.))

    @staticmethod
    def combine_matrices(trans, scale, rot):
        return np.dot(trans, np.dot(scale, rot))
