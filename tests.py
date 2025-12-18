
from graph import Graph
from bfs import bfs

def test_bfs():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    assert bfs(g, "A") == ["A", "B", "C"]
