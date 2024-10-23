"""
biconnected
1. Any vertex on the graph can reach other vertex.
2. After removing an node, the graph is still connected

-> graph doesn't have articulation point
"""

from collections import defaultdict

class BC:
    def is_bc(self, edges, n):
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.time = -1
        parent = -1
        src = 0
        self.disc = [-1]*n
        self.low = [0]*n
        if self.dfs(src, parent):
            return False
        if any(t == -1 for t in self.disc):
            return False
        return True

    def dfs(self, u, parent):
        self.time += 1
        self.low[u] = self.time
        self.disc[u] = self.time
        child = 0
        for v in self.graph[u]:
            if self.disc[v] == -1:
                child += 1
                if self.dfs(v, u):
                    return True
                self.low[u] = min(self.low[u], self.low[v])
                if parent == -1 and child == 2:
                    return True
                if parent != -1 and self.low[v] >= self.disc[u]:
                    return True
            elif parent != u:
                self.low[u] = min(self.low[u], self.disc[v])
        return False
