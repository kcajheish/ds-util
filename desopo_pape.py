from collections import deque

def shortest_path(src, edges, n):
    INF = 10**20
    d = [INF]*n
    p = [-1]*n
    m = [2]*n
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    q = deque([src])
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                p[v] = u
                if m[v] == 2:
                    m[v] = 1
                    q.append(v)
                elif m[v] == 0:
                    m[v] = 1
                    q.appendleft(v)
    return d
