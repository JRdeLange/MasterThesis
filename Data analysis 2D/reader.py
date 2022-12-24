from record import Record
from agentdata import AgentData

class Reader:

    def __init__(self):
        pass

    def construct_records(self, filename):
        record = Record()
        nr_of_slices = None

        tick = None
        boids_eaten = None
        predator = []
        boids = []

        with open(filename, "r") as file:
            # Get nr of slices
            nr_of_slices = int(file.readline())
            # Get rid if rest of header
            line = file.readline()
            while line[0] != '-':
                line = file.readline()

            for i in range(nr_of_slices):
                self.read_slice(file)


    def read_slice(self, file):
        tick = int(file.readline())
        boids_eaten = int(file.readline)
        pos = self.parse_tuple(file.readline())

        predator = AgentData(x, y)

        line = file.readline()
        while line[0] != '-':
            pos = line.split()
            rot = float(file.readline())



    def parse_tuple(self, line):
        line = line.split()
        x = float(line[1])
        y = float(line[2][:-1])
        return [x, y]





