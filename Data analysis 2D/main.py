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
    main()
