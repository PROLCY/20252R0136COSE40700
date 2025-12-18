
import heapq
from constants import INF

def dijkstra(graph, start):
    dist = {k: INF for k in graph.nodes}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph.get_neighbors(u).items():
            if dist[v.name] > d + w:
                dist[v.name] = d + w
                heapq.heappush(pq, (dist[v.name], v.name))
    return dist
