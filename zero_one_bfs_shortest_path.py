from collections import deque

def shortest_path(edges, n, src):
    graph = [[] for  _ in range(n)]
    INF = 10**20
    dist = [INF]*n
    dist[src] = 0
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    q = deque([src])
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if w == 0:
                    q.appendleft(v)
                else:
                    q.append(v)
    return dist


