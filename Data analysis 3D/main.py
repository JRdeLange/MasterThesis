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
    record = analysis.construct_experiment_analysis_file("test4.txt")

    analysis.plot_eaten_boids(record)
    #record = analysis.construct_experiment_analysis_file("exp_2D_rec_control_15_other_boids.txt")
    clusterer.cluster_and_plot(record.slices[0].boids_pos)
    clusterer.cluster_and_plot(record.slices[1].boids_pos)
    clusterer.cluster_and_plot(record.slices[2].boids_pos)
    clusterer.cluster_and_plot(record.slices[3].boids_pos)
    clusterer.cluster_and_plot(record.slices[4].boids_pos)


if __name__ == '__main__':
    main()
