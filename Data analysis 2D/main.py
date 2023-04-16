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


def ingest_all():
    nr_neighbours = [0, 1, 2, 5]
    for nr in nr_neighbours:
        folder = "/__exp small network " + str(nr) + " observed"
        analysis.mass_ingest_experiment("./raw_exps/set 1" + folder, "./exps/set 1" + folder)
        analysis.mass_ingest_experiment("./raw_exps/set 1 2" + folder, "./exps/set 1 2" + folder)
        analysis.mass_ingest_experiment("./raw_exps/set 2" + folder, "./exps/set 2" + folder)
        analysis.mass_ingest_experiment("./raw_exps/set 3" + folder, "./exps/set 3" + folder)


def print_data(folder, ready_for_table=False):
    # folder = "exps/set 1 2/__exp small network 5 observed"
    for filename in os.listdir(folder):
        file = folder + "/" + filename
        file = open(file)
        data = json.load(file)
        if ready_for_table:
            print("{}\t{}\t{:.3f} ({:.3f})\t{:.3f} ({:.3f})\t{:.3f} ({:.3f})".format(data["sum_boids_eaten"], data["total_nr_of_clusters"],
                                                                data["avg_cluster_size"], data["cluster_size_std_dev"], data["avg_pos_deviation"],
                                                                data["pos_deviation_std_dev"],
                                                                data["avg_rot_deviation"],
                                                                data["rot_deviation_std_dev"]).replace(".", ","))
        else:
            print("{}\t{}\t{:,}\t{:,}\t{:,}\t{:,}\t{:,}".format(data["sum_boids_eaten"], data["total_nr_of_clusters"],
                                                                data["avg_cluster_size"], data["avg_pos_deviation"],
                                                                data["pos_deviation_std_dev"],
                                                                data["avg_rot_deviation"],
                                                                data["rot_deviation_std_dev"]).replace(".", ","))


def print_entire_set(set_folder):
    for observed_folder in os.listdir(set_folder):
        folder = set_folder + "/" + observed_folder
        print_data(folder, ready_for_table=True)
        print("")
        print("")


def main():
    folder = "exps/best set/__exp small network 5 observed"
    print_data(folder, ready_for_table=False)

    '''
    record = reader.construct_records("raw_exps/__exp small network 0 observed/2D_rec_20_total_boids_slower_short_chase.txt")

    for x in range(51, 70):
        analysis.stats_for_slice(record.slices[x])
        positions = record.slices[x].boids_pos
        rotations = record.slices[x].boids_rotation
        clustering = clusterer.cluster(positions)
        clusters = clusterer.clustering_to_list_of_lists(clustering, positions, rotations)

        utils.plot_arrows(clusters)'''

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
