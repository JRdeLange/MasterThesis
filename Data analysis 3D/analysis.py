import utils
import matplotlib.pyplot as plt
import clusterer
import reader
from record import Record
import os
import json
import scipy.stats as stats
import pingouin
import numpy as np

def construct_experiment_analysis_file(name):
    record = reader.construct_records(name)

    sum_size_of_clusters = 0
    all_cluster_sizes = []
    total_nr_of_clusters = 0
    sum_pos_deviation = 0
    all_pos_deviations = []
    sum_rot_deviation = 0
    all_rot_deviations = []
    sum_boids_eaten = 0

    # for each slice
    for i, slice in enumerate(record.slices):

        clustering = clusterer.cluster(slice.boids_pos)
        clusters_pos = clusterer.clustering_to_list_of_lists(clustering, slice.boids_pos)
        clusters_rot = clusterer.clustering_to_list_of_lists(clustering, slice.boids_rotation)

        # things to calculate
        for idx in range(1, len(clusters_pos)):
            total_nr_of_clusters += 1

            # avg size of clusters
            cluster_size = len(clusters_pos[idx])
            sum_size_of_clusters += cluster_size
            all_cluster_sizes.append(cluster_size)
            # avg pos deviation within clusters
            pos_deviation = average_pos_deviation(clusters_pos[idx])
            sum_pos_deviation += pos_deviation
            all_pos_deviations.append(average_pos_deviation(clusters_pos[idx]))

            # avg rot deviation within clusters
            rot_deviation = average_rot_deviation(clusters_rot[idx])
            sum_rot_deviation += rot_deviation
            all_rot_deviations.append(rot_deviation)

            sum_boids_eaten += slice.boids_eaten

        if i % 1000 == 0:
            print("Analysing", str(i), "out of", len(record.slices))

    print(total_nr_of_clusters)

    # Things to calculate after the fact

    # Standard deviations
    cluster_size_std_dev = stats.tstd(all_cluster_sizes)
    pos_deviation_std_dev = stats.tstd(all_pos_deviations)
    rot_deviation_std_dev = stats.tstd(all_rot_deviations)

    json_dict = {
        "sum_size_of_clusters": sum_size_of_clusters,
        "all_cluster_sizes": all_cluster_sizes,
        "cluster_size_std_dev": cluster_size_std_dev,
        "total_nr_of_clusters": total_nr_of_clusters,
        "sum_pos_deviation": sum_pos_deviation,
        "all_pos_deviations": all_pos_deviations,
        "pos_deviation_std_dev": pos_deviation_std_dev,
        "sum_rot_deviation": sum_rot_deviation,
        "all_rot_deviations": all_rot_deviations,
        "rot_deviation_std_dev": rot_deviation_std_dev,
        "sum_boids_eaten": sum_boids_eaten
    }

    # Write to file
    if not os.path.exists("exps/" + name[:-4]):
        os.mkdir("exps/" + name[:-4])
    with open("exps/" + name[:-4] + "/exp_analysis_" + str(name), "w") as f:
        json.dump(json_dict, f)

    return record


def compare_jsons(a, b):
    a = json.load("exps/" + a)
    b = json.load("exps/" + b)
    data_a = [a["all_cluster_sizes"], a["all_pos_deviations"], a["all_rot_deviations"]]
    data_b = [b["all_cluster_sizes"], b["all_pos_deviations"], b["all_rot_deviations"]]
    # Transpose lists
    data_a = [list(x) for x in zip(*data_a)]
    data_b = [list(x) for x in zip(*data_b)]
    result = pingouin.multivariate_ttest(data_a, data_b)


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

def average_pos_deviation(data):
    # calc pairwise distance between all boids. We do it twice/both ways but that shouldn't matter
    total_distance = 0
    n = len(data) * (len(data) - 1)
    for boid_a in data:
        for boid_b in data:
            if boid_a is not boid_b:
                total_distance += utils.wrapping_distance_boids(boid_a, boid_b)
    return total_distance / n

def average_rot_deviation(data):
    # Calc average rotation by calculating avg cartesian coordinate
    n = len(data)
    x_sum = 0
    y_sum = 0
    for boid in data:
        cartesian = utils.rad_to_cartesian(boid)
        x_sum += cartesian[0]
        y_sum += cartesian[1]

    if x_sum == 0 and y_sum == 0:
        print("Avg rotation is undefined")
        return None

    avg_cartesian = [x_sum / n, y_sum / n]
    avg_cartesian = utils.normalize(avg_cartesian)
    avg_rad = utils.cartesian_to_rad(avg_cartesian)

    # Now calc avg deviation from avg rotation
    total_distance = 0
    for boid in data:
        total_distance += abs(utils.wrapping_distance_radians(boid, avg_rad))
    return total_distance / n

def average_cluster_size(data):
    clusters = clusterer.clustering_to_list_of_lists(clusterer.cluster(data), data)
    total = 0
    for x in range(1, len(clusters)):
        total += len(clusters[x])

    return total / (len(clusters) - 1)






