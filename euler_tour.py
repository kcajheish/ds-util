"""
tree
    Graph with N node and N-1 edges
    In dfs tree
        each node has one parent
        each node may have many children
euler tour
    nodes that are visted
    2N-1 nodes in the path
        For each edge, from and to nodes are visited one each
        Root node is starting point
        2*(N-1) + 1 = 2N-1

time O(E+V)
    E = number of edges
    V = number of nodes
"""
from collections import defaultdict

def euler_tour(edges, n, root):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    euler_tour = [-1]*(2*n-1)
    def dfs(node, index, euler_tour, adj):
        """
        Given a node
            update tour when node is first visited
            recursively visit children and update tour when call returns from children
        Return
            next position in the tour to the parent.
        """
        euler_tour[index] = node

        # root at the start of tour won't have parent
        parent = euler_tour[index-1] if index > 0 else -1
        for neigh in adj[node]:
            if neigh != parent:
                index = dfs(neigh, index+1, euler_tour, adj)
                euler_tour[index] = node
        return index+1
    dfs(root, 0, euler_tour, adj)
    return euler_tour

