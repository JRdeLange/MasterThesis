import pyglet


class Models:
    # boid_model = pyglet.graphics.vertex_list(6, ('v3f', (0, 1, 0, -0.7, -1, 0, 0, -0.7, 0,
    #                                                     0, 1, 0, 0, -0.7, 0, 0.7, -1, 0,)))

    boid_indices = [0, 9, 1, 1, 9, 2, 2, 9, 3, 3,
                    9, 4, 4, 9, 5, 5, 9, 6, 6, 9,
                    7, 7, 9, 8, 8, 9, 10, 10, 9, 11,
                    11, 9, 12, 12, 9, 13, 13, 9, 14,
                    14, 9, 15, 15, 9, 16, 16, 9, 17,
                    17, 9, 18, 18, 9, 19, 19, 9, 20,
                    20, 9, 21, 21, 9, 22, 22, 9, 23,
                    23, 9, 24, 24, 9, 25, 25, 9, 26,
                    26, 9, 27, 27, 9, 28, 28, 9, 29,
                    29, 9, 30, 30, 9, 31, 31, 9, 32,
                    32, 9, 0, 16, 24, 32, 32, 0, 1,
                    1, 2, 3, 3, 4, 5, 5, 6, 3, 7, 8,
                    10, 10, 11, 12, 12, 13, 16, 14, 15,
                    16, 16, 17, 18, 18, 19, 16, 20, 21,
                    24, 22, 23, 24, 24, 25, 28, 26, 27,
                    28, 28, 29, 30, 30, 31, 32, 32, 1,
                    7, 3, 6, 7, 7, 10, 16, 13, 14, 16,
                    16, 19, 20, 21, 22, 24, 25, 26, 28,
                    28, 30, 24, 1, 3, 7, 10, 12, 16,
                    16, 20, 24, 24, 30, 32, 32, 7, 16]

    boid_vertices = (0.000000, -0.759786, -0.650000,
                     0.126809, -0.759786, -0.637510,
                     0.248744, -0.759786, -0.600522,
                     0.361121, -0.759786, -0.540455,
                     0.459619, -0.759786, -0.459619,
                     0.540455, -0.759786, -0.361121,
                     0.600522, -0.759786, -0.248744,
                     0.637510, -0.759786, -0.126809,
                     0.650000, -0.759786, -0.000000,
                     0.000000, 1.240214, -0.000000,
                     0.637510, -0.759786, 0.126809,
                     0.600522, -0.759786, 0.248744,
                     0.540455, -0.759786, 0.361121,
                     0.459619, -0.759786, 0.459619,
                     0.361121, -0.759786, 0.540455,
                     0.248744, -0.759786, 0.600522,
                     0.126809, -0.759786, 0.637510,
                     -0.000000, -0.759786, 0.650000,
                     -0.126809, -0.759786, 0.637510,
                     -0.248744, -0.759786, 0.600522,
                     -0.361121, -0.759786, 0.540455,
                     -0.459620, -0.759786, 0.459619,
                     -0.540456, -0.759786, 0.361120,
                     -0.600522, -0.759786, 0.248744,
                     -0.637510, -0.759786, 0.126808,
                     -0.650000, -0.759786, -0.000001,
                     -0.637510, -0.759786, -0.126809,
                     -0.600521, -0.759786, -0.248745,
                     -0.540455, -0.759786, -0.361121,
                     -0.459619, -0.759786, -0.459620,
                     -0.361120, -0.759786, -0.540456,
                     -0.248743, -0.759786, -0.600522,
                     -0.126808, -0.759786, -0.637511,)

    cube_indices = [0, 1, 1, 2, 2, 3, 3, 0,
                    4, 7, 7, 6, 6, 5, 5, 4,
                    0, 4, 4, 5, 5, 1, 1, 0,
                    1, 5, 5, 6, 6, 2, 2, 1,
                    2, 6, 6, 7, 7, 3, 3, 2,
                    4, 0, 0, 3, 3, 7, 7, 4]

    cube_vertices = (1.000000, -1.000000, -1.000000,
                     1.000000, -1.000000, 1.000000,
                     -1.000000, -1.000000, 1.000000,
                     -1.000000, -1.000000, -1.000000,
                     1.000000, 1.000000, -1.000000,
                     1.000000, 1.000000, 1.000000,
                     -1.000000, 1.000000, 1.000000,
                     -1.000000, 1.000000, -1.000000)

    boid_model = pyglet.graphics.vertex_list_indexed(int(len(boid_vertices) / 3),
                                                     boid_indices,
                                                     ('v3f/static', boid_vertices))

    wireframe_world_cube = pyglet.graphics.vertex_list_indexed(int(len(cube_vertices) / 3),
                                                               cube_indices,
                                                               ('v3f/static', cube_vertices))
