from sklearn.cluster import _dbscan
from reader import Reader
from record import Record

def main():
    # Read in file
    filename = "test.txt"
    reader = Reader()
    record:Record = reader.construct_records("test.txt")

    [print(slice.predator_rotation) for slice in record.slices]

if __name__ == '__main__':
    main()
