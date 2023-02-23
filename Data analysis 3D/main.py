import random
import analysis
import statistics
import clusterer
import reader
import math
from sklearn.cluster import DBSCAN
import numpy as np
import utils


def main():
    # Read in file
    analysis.construct_experiment_analysis_file("2D_rec_10_total_boids4.txt")

    record = reader.construct_records("2D_rec_10_total_boids4.txt")
    statistics.test()
    analysis.plot_eaten_boids(record)
    #record = analysis.construct_experiment_analysis_file("exp_2D_rec_control_15_other_boids.txt")
    clusterer.cluster_and_plot(record.slices[20].boids_pos)
    clusterer.cluster_and_plot(record.slices[22].boids_pos)
    clusterer.cluster_and_plot(record.slices[23].boids_pos)
    clusterer.cluster_and_plot(record.slices[24].boids_pos)
    clusterer.cluster_and_plot(record.slices[25].boids_pos)


if __name__ == '__main__':
    # main()
    data = [[[0, 0, 0], [-1, -0.5, -0.7], [0.8, 0.8, 0.5], [0.126, 0.558, 0.372], [0.952, 0.905, -0.186], [0.06, -0.156, 0.542], [-0.227, -0.874, -0.381], [0.615, 0.649, -0.518], [0.388, 0.631, 0.564], [-0.53, -0.775, 0.409], [0.187, -0.537, 0.919], [-0.328, 0.854, -0.155]],
        [[0.2, 0.2, 0.2], [0.1, 0.1, 0.1], [0.2, 0.1, 0.3], [-0.006, -0.595, 0.891], [-0.342, 0.18, -0.59], [-0.385, -0.529, -0.86], [-0.714, 0.338, 0.677], [0.121, -0.704, 0.343], [0.244, -0.618, -0.36], [-0.235, -0.331, 0.524], [-0.301, 0.267, 0.711], [0.536, 0.639, 0.195]],
        [[0.5, 0.8, 0.8], [0.6, 0.8, 0.75], [0.982, 0.277, -0.324], [0.925, 0.89, 0.282], [0.448, 0.433, 0.689], [0.671, 0.587, 0.466], [-0.031, 0.777, 0.381], [0.858, -0.412, -0.831], [-0.336, 0.864, -0.033], [0.312, 0.832, 0.52], [-0.006, 0.837, -0.59], [0.825, 0.657, -0.597]]]
    utils.plot_points(data)
