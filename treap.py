"""
height ~log(N), N: number of keys
- checkout random binary tree & treap on wiki

Tree
- Inorder traversal gives keys in ascending order.

Max Heap structure.
- Each node is assigned with random priority.
- Parent node has higher priority
"""
import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.priority = random.random()

class Treap:
    def __init__(self):
        self.root = None

    def search(self, node, key):
        if node is None or node.key == key:
            return node

        visit_node = node.left if node.key > key else node.right
        return self.search(visit_node, key)

    def insert(self, node, key):
        if not node:
            return Node(key)
        if node.key > key:
            node.left = self.insert(node.left, key)
            if node.priority < node.left.priority:
                self.right_rotate(node)
        else:
            node.right = self.insert(node.right, key)

            if node.priority > node.right.priority:
                self.left_rotate(node)
        return node

    def delete(self, node, key):
        if not node:
            return node

        if key > node.key:
            self.delete(node.right, key)
        elif key < node.key:
            self.delete(node.left, key)
        elif not node.left:
            node = node.right
        elif not node.right:
            node = node.left
        elif node.right.priority > node.left.priority:
            node = self.rotate_left(node)
            node.left = self.delete(node.left, key)
        elif node.left.priority < node.left.priority:
            node = self.rotate_right(node)
            node.right = self.delete(node.right, key)
        return node

    def left_rotate(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        return right

    def right_rotate(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        return left
