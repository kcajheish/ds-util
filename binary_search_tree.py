class Node:
    def __init__(self, key, value, N):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.N = N


class BST:
    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if not node:
            return 0
        return node.N

    def get(self, key):
        node = self._get(self.root, key)
        if not node:
            return None
        return node.value

    def _get(self, node, key):
        if not node:
            return None
        if node.key > key:
            self._get(node.left, key)
        elif node.key < key:
            self._get(node.right, key)
        else:
            return node


    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if not node:
            return Node(key, value, 1)

        if node.key > key:
            node.left = self._put(node.left, key, value)
        elif node.key < key:
            node.right = self._put(node.right, key, value)
        else:
            node.key = key
            node.value = value

        node.N = self._size(node.left) + self._size(node.right) + 1

        return node

    def delete(self, node, key):
        if not node:
            return None

        if node.key < key:
            node.right = self.delete(node.right, key)
            node.N = self._size(node.right) + self._size(node.left)
        elif node.key > key:
            node.left = self.delete(node.left, key)
            node.N = self._size(node.right) + self._size(node.left)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                successor = self.min_node(node.right)
                node.right = self.delete(node.right, successor.key)
                node = successor

        node.N = max(self._size(node.left), self._size(node.right))
        return node

    def min_node(self, node):
        while node.left:
            node = node.left
        return node
