import queue
from copy import deepcopy


class History:

    def __init__(self):
        self.q = queue.Queue(3)

    def add(self, pos):
        self.q.get()
        self.q.put(deepcopy(pos))

    def fill(self, pos):
        self.q = queue.Queue(3)
        for x in range(3):
            self.q.put(deepcopy(pos))

    def get(self):
        return [self.q.queue[0], self.q.queue[1], self.q.queue[2]]