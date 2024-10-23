class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

class KDimensionalTree:
    def __init__(self):
        self.root = None

    def delete(self, node, point, depth):
        k = self.k
        dimension = depth % k
        if self.same(node.point, point):
            if node.right:
                min_node = self.min(depth+1, node.right, dimension)
                node.point = min_node.point
                node.right = self.delete(node.right, min_node.point, depth+1)
            elif node.left:
                min_node = self.min(depth+1, node.left, dimension)
                node.point = min_node.point
                node.right = self.delete(node.left, min_node.point, depth+1)
            else:
                del node
                return None
        else:
            if point[dimension] >= node.point[dimension]:
                self.delete(node.right, point, depth+1)
            else:
                self.delete(node.left, point, depth+1)
        return node

    def min(self, depth, node, target_dimension):
        if node is None:
            return float('inf')
        k = self.k
        dimension = depth % k
        if dimension == target_dimension:
            return min(
                node.point[target_dimension],
                self.min(depth+1, node.left, target_dimension)
            )
        else:
            return min(
                self.min(depth+1, node.left, target_dimension),
                self.min(depth+1, node.right, target_dimension),
                node.point[target_dimension]
            )

    def insert(self, point):
        if not self.root:
            self.root = Node(point)
            return
        parent = None
        node = self.root
        k = self.k
        depth = 0
        while node:
            dimension = depth % k
            parent = node
            if point[dimension] >= node.point[dimension]:
                node = node.right
            else:
                node = node.left
            depth += 1
        new_node = Node(point)
        if point[dimension] >= parent[dimension]:
            parent.right = new_node
        else:
            parent.left = new_node

    def search(self, point):
        node = self.root
        k = self.k
        depth = 0
        while node:
            if self.same(node.point, point):
                return True
            current_dimensional = depth % k
            if point[current_dimensional] >= node.point[current_dimensional]:
                node = node.right
            else:
                node = node.left
            depth += 1
        return False

    def same(self, a, b):
        k = len(a)
        return all(a[i] == b[i] for i in range(k))


