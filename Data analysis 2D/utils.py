import math
import numpy as np
import matplotlib.pyplot as plt

colors = ['#000000', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
          '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5']

two_pi = 2 * math.pi

def rad_to_cartesian(rot):
    x = math.cos(rot)
    y = math.sin(rot)
    return [x, y]

def cartesian_to_rad(vec):
    return math.atan2(vec[1], vec[0])

def distance_2d(a, b):
    delta_x = abs(a[0] - b[0])
    delta_y = abs(a[1] - b[1])
    distance = math.sqrt(delta_x * delta_x + delta_y * delta_y)
    return distance

def normalize(vec):
    scalar = 0
    for element in vec:
        scalar += element*element
    scalar = math.sqrt(scalar)
    newvec = []
    for element in vec:
        newvec.append(element / scalar)
    return newvec

def wrapping_distance_radians(origin, to):
    nothing = to - origin
    minus = (to - two_pi) - origin
    if abs(minus) < abs(nothing):
        return minus
    plus = (to + two_pi) - origin
    if abs(plus) < abs(nothing):
        return plus
    return nothing

# Bit for wrapping distance

def vec2_magnitude(vec):
    return np.sqrt(vec[0]*vec[0] + vec[1]*vec[1])

def wrapping_distance_boids(origin, to):
    vec = [0, 0]
    # Construct all options
    x_options = [to[0] - 2, to[0], to[0] + 2]
    y_options = [to[1] - 2, to[1], to[1] + 2]
    # Construct vector
    vec[0] = best_option(origin[0], x_options)
    vec[1] = best_option(origin[1], y_options)
    return vec2_magnitude(vec)

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

def plot_points(points_lists):
    # Get number of lists
    num_lists = len(points_lists)
    # Use a different color for each inner list
    for i in range(num_lists):
        x = [point[0] for point in points_lists[i]]
        y = [point[1] for point in points_lists[i]]
        plt.scatter(x, y, c=colors[i])
    plt.xlim([-1, 1])
    plt.ylim([-1, 1])
    plt.show()