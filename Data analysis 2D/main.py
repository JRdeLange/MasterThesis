import json
import random
import analysis
import statistics
import clusterer
import reader
import math
from sklearn.cluster import DBSCAN
import numpy as np
import utils
import json
import os


def main():

    folder = "exps/small network 0 observed"
    for filename in os.listdir(folder):
        file = folder + "/" + filename
        file = open(file)
        data = json.load(file)
        print(data["sum_boids_eaten"], data["total_nr_of_clusters"], data["avg_cluster_size"], data["avg_pos_deviation"], data["pos_deviation_std_dev"], data["avg_rot_deviation"], data["rot_deviation_std_dev"])


    '''# Read in file
    analysis.construct_experiment_analysis_file("2D_rec_10_total_boids4.txt")

    record = reader.construct_records("2D_rec_10_total_boids4.txt")
    statistics.test()
    analysis.plot_eaten_boids(record)
    #record = analysis.construct_experiment_analysis_file("exp_2D_rec_control_15_other_boids.txt")
    clusterer.cluster_and_plot(record.slices[20].boids_pos)
    clusterer.cluster_and_plot(record.slices[22].boids_pos)
    clusterer.cluster_and_plot(record.slices[23].boids_pos)
    clusterer.cluster_and_plot(record.slices[24].boids_pos)
    clusterer.cluster_and_plot(record.slices[25].boids_pos)'''


if __name__ == '__main__':
    main()
