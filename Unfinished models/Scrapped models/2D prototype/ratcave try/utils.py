#https://stackoverflow.com/questions/54188353/how-do-i-make-3d-in-pyglet
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

