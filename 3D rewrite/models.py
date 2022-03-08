import pyglet


class Models:
    boid_model = pyglet.graphics.vertex_list(6, ('v3f', (0, 1, 0, -0.7, -1, 0, 0, -0.7, 0,
                                                         0, 1, 0, 0, -0.7, 0, 0.7, -1, 0,)))

    wireframe_world_cube = pyglet.graphics.vertex_list