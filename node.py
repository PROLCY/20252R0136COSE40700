
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, node, weight=1):
        self.neighbors[node] = weight
