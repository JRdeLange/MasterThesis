import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np
import utils

eps = 0.4
min_samples = 3
metric = utils.wrapping_distance_boids


def cluster(data):
    clustering = DBSCAN(eps=eps, min_samples=min_samples, metric=metric).fit(data)
    return clustering

def clustering_to_list_of_lists(clustering, pos_data, rot_data=None):
    labels = clustering.labels_
    n_clusters = labels.max() + 2
    clusters = []

    for x in range(n_clusters):
        clusters.append([])
    for idx, point in enumerate(pos_data):
        new_entry = point
        if rot_data:
            new_entry = [point, rot_data[idx]]
        clusters[labels[idx]+1].append(new_entry)

    return clusters

def cluster_and_plot(data):
    clustering = cluster(data)
    clusters = clustering_to_list_of_lists(clustering, data)
    utils.plot_points(clusters)
