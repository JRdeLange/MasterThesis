import utils
import matplotlib.pyplot as plt


def plot_eaten_boids(record, bin_size=5000):
    x = []
    y = []
    idx = None
    for i, slice in enumerate(record.slices):
        # if not still at the previous entry, add a new one
        if idx != int(slice.tick / bin_size):
            idx = int(slice.tick / bin_size)
            x.append((idx + 1) * bin_size)
            y.append(0)
        # current entry exists
        y[idx] += slice.boids_eaten
    plt.plot(x, y)
    plt.show()

def average_pos_deviation(set):
    # calc pairwise distance between all boids. We do it twice/both ways but that shouldn't matter
    total_distance = 0
    n = len(set) * (len(set) - 1)
    for boid_a in set:
        for boid_b in set:
            if boid_a is not boid_b:
                total_distance += utils.distance_2d(boid_a, boid_b)
    return total_distance / n

def average_rot_deviation(set):
    # Calc average rotation by calculating avg cartesian coordinate
    n = len(set)
    x_sum = 0
    y_sum = 0
    for boid in set:
        cartesian = utils.rad_to_cartesian(boid)
        print(cartesian)
        x_sum += cartesian[0]
        y_sum += cartesian[1]

    if x_sum == 0 and y_sum == 0:
        print("Avg rotation is undefined")
        return None

    avg_cartesian = [x_sum / n, y_sum / n]
    avg_cartesian = utils.normalize(avg_cartesian)
    print(avg_cartesian)
    avg_rad = utils.cartesian_to_rad(avg_cartesian)
    print(avg_rad)

    # Now calc avg deviation from avg rotation
    total_distance = 0
    for boid in set:
        total_distance += abs(utils.wrapping_distance_radians(boid, avg_rad))
    return total_distance / n





