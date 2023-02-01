# Contains all relevant agent info needed for the distance matrix

class AgentInfo:
    def __init__(self, agent, direction, dist):
        self.agent = agent
        self.direction = direction
        self.dist = dist
