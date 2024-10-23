from collections import defaultdict

class Tarjan:
    def scc(self, edges, n):
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
        self.time = 0
        self.stack = [False]*n
        self.que = []
        self.low = [-1]*n
        self.disc = [-1]*n
        self.ans = []

        for u in range(n):
            if self.disc[u] == -1:
                self.dfs(u)
        return self.ans[:]

    def dfs(self, u):
        self.time += 1
        self.low[u] = self.time
        self.disc[u] = self.time
        self.stack[u] = True
        self.que.append(u)
        for v in self.graph[u]:
            if self.disc[v] == -1:
                self.dfs(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif self.stack[v]:
                # u -> v is a backedge
                self.low[u] = min(self.low[u], self.disc[v])
            else:
                # cross edge; u, v are in different dfs tree thus we do nothing
                pass

        # found the root of dfs subtree
        if self.low[u] == self.disc[u]:
            w = -1
            component = []
            while self.que[w] != u:
                w = self.que.pop()
                component.append(w)
                self.stack[w] = False
            self.ans.append(component)
