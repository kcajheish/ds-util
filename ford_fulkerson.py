from collections import deque
class FordFulkerson:
    """
    edges: u, v, capacity
    """
    def bfs(self, source, target):
        graph = self.graph
        parent = self.parent
        capacity = self.capacity
        q = deque([source, float('inf')])
        while q:
            node, min_flow = q.popleft()
            for next_node in graph[node]:
                if parent[next_node] == -1 and capacity[node][next_node] > 0:
                    parent[next_node] = node
                    min_flow = min(min_flow, capacity[node][next_node])
                    if next_node == target:
                        return min_flow
                    q.append([next_node, min_flow])
        return 0


    def max_flow(self, edges, n, source, target):
        self.graph = [[] for i in range(n)]
        self.capacity = [[0]*n for _ in range(n)]
        for u, v, capacity in edges:
            self.graph[u].append(v)
            self.capacity[u][v] = capacity
        self.parent = [-1]*n
        max_flow = 0
        while min_flow := self.bfs(source, target):
            max_flow += min_flow
            current = target
            while current != source:
                p = self.parent[current]
                self.capacity[p][current] -= min_flow
                self.capacity[current][p] += min_flow
                current = p
        return max_flow
