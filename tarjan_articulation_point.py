"""
Removal of one vertex increase number of components
"""
from collections import defaultdict

class Bridge:
    def points(self, edges, n):
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.time = 0
        self.disc = [-1]*n
        self.low = [0]*n
        parent = -1
        src = 0
        self.articulation_points = []
        for i in range(n):
            if self.disc[i] == -1:
                self.dfs(src, parent)

    def dfs(self, u, parent):
        self.time += 1
        self.disc[u] = self.time
        self.low[u] = self.time
        children = 0
        for v in self.graph[v]:
            if self.disc[v] == -1:
                children += 1
                self.dfs(v, u)
                self.low[u] = min(self.low[u], self.low[v])
                if parent != -1 and self.low[v] >= self.disc[u]:
                    self.articulation_points.append(u)

                if parent == -1 and children == 2:
                    self.articulation_points.append(u)

            elif v != parent:
                self.low[u] = min(self.low[u], self.disc[v])

