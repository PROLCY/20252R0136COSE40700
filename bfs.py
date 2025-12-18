
from collections import deque

def bfs(graph, start):
    visited = set()
    order = []
    q = deque([start])

    while q:
        u = q.popleft()
        if u in visited:
            continue
        visited.add(u)
        order.append(u)
        for v in graph.get_neighbors(u):
            q.append(v.name)
    return order
