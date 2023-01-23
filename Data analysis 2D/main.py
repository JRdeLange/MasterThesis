from sklearn.cluster import _dbscan
from reader import Reader
from record import Record
import analysis
import math

def main():
    # Read in file
    filename = "only_the_one14.txt"
    reader = Reader()
    record: Record = reader.construct_records(filename)
    analysis.plot_eaten_boids(record, bin_size=50000)
    #[print(slice.predator_rotation) for slice in record.slices]



if __name__ == '__main__':
    main()
