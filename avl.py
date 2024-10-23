"""
AVL
Self-balancing binary search tree
For all node, diff(height of left subtree, height of right subtree) <= 1
left_child.key < root.key < right_child.key

For normal binary search tree, operation takes O(h). If a tree is skewed, h ~= N.
Thus, AVL tree is always balanced and have O(logN) time.


        y                                       x
      /    \                                   /  \
    x       T3     right rotate ----->       T1    y
  /  \                                            /  \
T1    T2           left rotate <------           T2   T3
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def right_rotate(self, y):
        x = y.left
        subtree = x.right

        x.right = y
        y.left = subtree

        y.height = max(y.left.height, y.right.height) + 1
        x.height = max(x.left.height, x.right.height) + 1
        return x

    def left_rotate(self, x):
        y = x.right
        subtree = y.left

        x.right = subtree
        y.left = x

        x.height = max(self.h(x.left), self.h(x.right)) + 1
        y.height = max(self.h(y.left), self.h(y.right)) + 1

        return y

    def h(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.h(node.left) - self.h(node.right)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)

        if node.key < key:
            node.right = self.insert(node.right, key)
        elif node.key > key:
            node.left = self.insert(node.left, key)
        else:
            raise ValueError("duplicate keys")

        node.height = max(self.h(node.left), self.h(node.right)) + 1

        factor = self.balance_factor(node)

        # left-left
        if factor > 1 and key < node.left.key:
            node = self.right_rotate(node)

        # left-right
        if factor > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            node.right = self.right_rotate(node.right)

        # right-left
        if factor < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            node = self.left_rotate(node)

        # right-right
        if factor < -1 and key > node.right.key:
            node = self.left_rotate(node)

        return node

    def delete(self, node, key):
        if not node:
            return None

        if node.key < key:
            node.right = self.delete(node.right, key)
        elif node.key > key:
            node.left = self.delete(node.left, key)
        else:
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                successor = self.min_node(node.right)
                node.right = self.delete(node.right, successor.key)
                node = successor

        factor = self.balance_factor(node)

        # left-left
        if factor > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        # left-right
        if factor > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # right-right
        if factor < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        # right-left
        if factor < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # balanced
        return node

    def min_node(self, node):
        while node.left:
            node = node.left
        return node

    def pre_order(self):
        """
        this -> left -> right

        res.append(node.key)
        node.left = d
        """
        res = []
        stack = []
        node = self.root
        while node or stack:
            if not node:
                node = stack.pop()
            res.append(node.key)
            node = node.left
            if node.right:
                stack.append(node.right)
        return res
