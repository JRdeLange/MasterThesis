from reader import Reader
from record import Record
import random
import analysis
import clusterer
import math
from sklearn.cluster import DBSCAN
import numpy as np


def main():
    # Read in file
    filename = "only_the_one14.txt"
    reader = Reader()
    record: Record = reader.construct_records(filename)
    analysis.plot_eaten_boids(record, bin_size=50000)
    #[print(slice.predator_rotation) for slice in record.slices]



if __name__ == '__main__':
    data = []
    for x in range(1000):
        data.append([random.random()*30, random.random()*30])

    clustering = clusterer.cluster(data, 1, 1)
    clusters = clusterer.clustering_to_list_of_lists(clustering, data)
    print(clusters)
    clusterer.plot_points(clusters)

    #main()
