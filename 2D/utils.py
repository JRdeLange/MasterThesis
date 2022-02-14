#https://stackoverflow.com/questions/54188353/how-do-i-make-3d-in-pyglet
#https://github.com/01AutoMonkey/open.gl-tutorials-to-pyglet

import math


class Utils:

    @staticmethod
    def world_to_screen(renderer, world, x, y):
        win_x, win_y = renderer.window.get_size()
        dim_x, dim_y = world.get_size()
        x = x / dim_x * win_x
        y = y / dim_y * win_y
        return x, y

    @staticmethod
    def radians_to_vec(r):
        return math.sin(r), math.cos(r)

    @staticmethod
    def get_scale_matrix(x=1, y=1, z=1):
        return ((float(x), 0., 0., 0.),
                (0., float(y), 0., 0.),
                (0., 0., float(z), 0.),
                (0., 0., 0., 1.))

    @staticmethod
    def get_translate_matrix(x=0, y=0, z=0):
        return ((1., 0., 0., float(x)),
                (0., 1., 0., float(y)),
                (0., 0., 1., float(z)),
                (0., 0., 0., 1.))

    @staticmethod
    def get_identity_matrix():
        return ((1., 0., 0., 0.),
                (0., 1., 0., 0.),
                (0., 0., 1., 0.),
                (0., 0., 0., 1.))
