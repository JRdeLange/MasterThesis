import math

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
