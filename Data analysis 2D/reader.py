from record import Record
from agentdata import AgentData

def construct_records(filename):
    record = Record()

    with open(filename, "r") as file:
        # Get nr of slices
        nr_of_slices = int(file.readline())
        # Get rid of rest of header
        line = file.readline()
        while line[1] != '-':
            line = file.readline()

        for i in range(nr_of_slices):
            read_slice(file, record)
            if i%1000 == 0:
                print("Read slice " + str(i) + " out of " + str(nr_of_slices))

    print("Finished reading")
    return record

def read_slice(file, record):
    tick = int(file.readline())
    boids_eaten = int(file.readline())

    pos = file.readline()
    rot = file.readline()
    # Check for None (no predator)
    if pos[0] == "N":
        predator = AgentData(None, None)
    else:
        pos = parse_tuple(pos)
        rot = float(rot)
        predator = AgentData(pos, rot)

    boids = []
    line = file.readline()

    while line[1] != '-':
        pos = parse_tuple(line)
        rot = float(file.readline())
        boids.append(AgentData(pos, rot))
        line = file.readline()

    record.add_slice(tick, boids_eaten, predator, boids)

def parse_tuple(line):
    line = line.split(' ')
    return [float(number) for number in line]
