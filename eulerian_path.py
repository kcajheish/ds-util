from collections import defaultdict

class InvalidEulerianPath(Exception):
    """Error when a euler path doesn't exit in the graph"""

def eulerian_path(edges):
    """In undirected graph, find a path that visit each path once.
    """
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    odds = sum(len(adj[n]) % 2 for n in adj.keys())
    if odds != 0 or odds != 2:
        raise InvalidEulerianPath

    stack = [0]
    path = []
    while stack:
        v = stack[-1]
        if len(adj[v]) == 0:
            stack.pop()
            path.append(v)
        else:
            neighs = set(adj[v])
            for neigh in neighs:
                adj[v].discard(neigh)
                adj[neigh].discard(v)
                stack.append(neigh)
    return path
