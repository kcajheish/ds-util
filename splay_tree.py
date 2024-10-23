"""
search, insert, delete ~ O(logN)

splay
- rotate tree node
- make most recently accessed/inserted node new root
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right
        subtree = y.left
        y.left = x
        x.right = subtree
        return y

    def right_rotate(self, y):
        x = y.left
        subtree = x.right
        x.right = y
        y.left = subtree
        return x

    def splay(self, node, key):
        if not node or node.key == key:
            return node

        if node.key > key:
            if node.left is None:
                return node
            if node.left.key > node.key:
                node.left.left = self.splay(node.left.left, key)
                node = self.right_rotate(node)
            else:
                node.left.right = self.splay(node.left.right, key)
                if node.left.right:
                    node.left = self.left_rotate(node.left)
            return self.right_rotate(node) if node.left else node
        else:
            if node.right is None:
                return node
            if node.right.key < node.key:
                node.right.right = self.splay(node.right.right, key)
                self.left_rotate(node)
            else:
                node.right.left = self.splay(node.right.left, key)
                if node.right.left:
                    self.right_rotate(node.right)
            return self.left_rotate(node) if node.right else node

    def searh(self, key):
        return self.splay(self.root, key)

    def insert(self, key):
        root = self.root
        if not root:
            self.root = Node(key)
            return self.root

        root = self.splay(root, key)
        if root.key == key:
            return root

        new_node = Node(key)
        if root.key > key:
            new_node.left = root.left
            root.left = None
            new_node.right = root
        else:
            new_node.right = root.right
            root.right = None
            new_node.left = root

        self.root = new_node
        return self.root

    def delete(self, key):
        root = self.root
        if not root:
            return

        root = self.splay(root, key)

        if root.key != key:
            return

        if root.left is None:
            new_root = root.right
        else:
            # splay maximum node on the left subtree
            new_root = self.splay(root.left, key)
            new_root.right = root.right

        self.root = new_root
        del root
        return



    def pre_order(self):
        node = self.root
        stack = []
        res = []
        while node or stack:
            if not node:
                node = stack.pop()
            res.append(node.key)
            if node.right:
                stack.append(node.right)
            node = node.left
        return res
