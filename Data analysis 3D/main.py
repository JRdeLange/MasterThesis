import random
import analysis
import statistics
import clusterer
from record import Record
import reader
import math
from sklearn.cluster import DBSCAN
import numpy as np
import utils


def main():
    # Read in file
    record = analysis.construct_experiment_analysis_file("test4.txt")

    for idx in range(0, 3):
        clustering = clusterer.cluster(record.slices[idx].boids_pos)
        clusters = clusterer.clustering_to_list_of_lists(clustering, record.slices[idx].boids_pos, record.slices[idx].boids_rotation)
        utils.plot_arrows_3d(clusters)


    #analysis.plot_eaten_boids(record)
    #record = analysis.construct_experiment_analysis_file("exp_2D_rec_control_15_other_boids.txt")


if __name__ == '__main__':
    main()
