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
            # Get rid of rest of header
            line = file.readline()
            while line[1] != '-':
                line = file.readline()

            for i in range(nr_of_slices):
                self.read_slice(file, record)
                print("Read slice " + str(i) + " out of " + str(nr_of_slices))

        return record

    def read_slice(self, file, record):
        tick = int(file.readline())
        boids_eaten = int(file.readline())

        pos = self.parse_tuple(file.readline())
        rot = float(file.readline())
        predator = AgentData(pos, rot)

        boids = []
        line = file.readline()

        while line[1] != '-':
            pos = self.parse_tuple(line)
            rot = float(file.readline())
            boids.append(AgentData(pos, rot))
            line = file.readline()

        record.add_slice(tick, boids_eaten, predator, boids)

    def parse_tuple(self, line):
        line = line.split(' ')
        return [float(number) for number in line]
