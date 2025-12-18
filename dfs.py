
def dfs(graph, start):
    visited = set()
    order = []

    def _dfs(u):
        if u in visited:
            return
        visited.add(u)
        order.append(u)
        for v in graph.get_neighbors(u):
            _dfs(v.name)

    _dfs(start)
    return order
