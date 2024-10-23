from collections import defaultdict

class Brdige:
    def get(self, edges, n):
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.time = -1
        self.disc = [-1]*n
        self.low = [0]*n
        parent = -1
        self.bridges = []
        for i in range(n):
            if self.disc[i] == -1:
                self.dfs(i, parent)
        return self.bridges

    def dfs(self, u, parent):
        self.time += 1
        self.low[u] = self.time
        self.disc[u] = self.time
        for v in self.graph[u]:
            if self.disc[v] == -1:
                self.dfs(v, u)
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[u] < self.low[v]:
                    self.bridges.append((u, v))
            elif v != parent:
                self.low[u] = min(self.low[u], self.disc[v])
