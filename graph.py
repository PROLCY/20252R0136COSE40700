
from node import Node

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, u, v, w=1):
        if u not in self.nodes:
            self.nodes[u] = Node(u)
        if v not in self.nodes:
            self.nodes[v] = Node(v)
        self.nodes[u].add_neighbor(self.nodes[v], w)

    def get_neighbors(self, u):
        return self.nodes[u].neighbors
