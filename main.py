
from graph import Graph
from bfs import bfs
from dfs import dfs
from shortest_path import dijkstra

def main():
    g = Graph()
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("C", "D", 1)

    print("BFS:", bfs(g, "A"))
    print("DFS:", dfs(g, "A"))
    print("Shortest paths:", dijkstra(g, "A"))

if __name__ == "__main__":
    main()
