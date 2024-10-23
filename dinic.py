"""
time O(EV^2)

In residual graph, path from source to target doesn't exit
use bfs

layered network
- calculate level of v, the shortest path from s to v. Note that edges in the path must have positive capacity.

blocking flow
- For every path from s to t, at least one edge is saturated by this flow.

Residual capacity for each edge:
- C(u, v) = capacity - flow
- C(v, u) = flow

Terminiation ends in V phase.

steps
- construct layered network in residual G
- find blocking flow in layered network
- add to current flow
"""
from collections import deque
class Edge:
    def __init__(self, vertex, flow, capacity, rev):
        self.v = vertex
        self.flow = flow
        self.capacity = capacity
        self.rev = rev

class MaxFlow:

    def max_flow(self, edges, n, src, target):
        self.graph = [[] in range(n)]
        self.level = [-1]*n
        for u, v, c in edges:
            forward = Edge(v, 0, c, len(self.graph[v]))
            back = Edge(u, 0, 0, len(self.graph[u]))

        self.graph[v].append(forward)
        self.graph[u].append(back)

        if src == target:
            return -1

        total = 0
        while self.bfs(src, target):
            ptr = [0]*n
            if flow := self.send_flow(src, float('inf'), target, ptr):
                total += flow
        return total

    def bfs(self, s, t, n):
        for i in range(n):
            self.level[i] = -1
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for e in self.graph[u]:
                if self.level[e.v] == -1 and e.flow < e.capacity:
                    self.level[e.v] = self.level[u]+1
                q.append(e.v)
        return self.level[t] != -1

    def send_flow(self, u, flow, t, ptr):
        if u == t:
            return 0

        while ptr[u] < len(self.graph[u]):
            edge = self.graph[u][ptr[u]]
            if self.level[edge.v] == self.level[edge.u]+1 and edge.flow < edge.capacity:
                residual = min(flow, edge.capacity - edge.flow)
                current_flow = self.send_flow(edge.v, residual, t, ptr)
                if current_flow is not None and current_flow > 0:
                    edge.flow += current_flow
                    self.graph[edge.u][edge.rev].flow -= current_flow
                    return current_flow
            ptr[u] += 1




