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
    record = reader.construct_records("2D_rec_10_total_boids4.txt")
    analysis.plot_eaten_boids(record)
    #record = analysis.construct_experiment_analysis_file("exp_2D_rec_control_15_other_boids.txt")
    clusterer.cluster_and_plot(record.slices[200].boids_pos)
    clusterer.cluster_and_plot(record.slices[202].boids_pos)
    clusterer.cluster_and_plot(record.slices[203].boids_pos)
    clusterer.cluster_and_plot(record.slices[204].boids_pos)
    clusterer.cluster_and_plot(record.slices[205].boids_pos)
    statistics.test()


if __name__ == '__main__':
    main()
