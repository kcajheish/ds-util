"""
Time complexity depends on probability analysis
Bottom layer is linked list. layers above skip a few links.
Search, insertion, deletion takes O(logN).
"""
import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None]*(level+1) # zero start with 0

class SkipList:
    def __init__(self, p, max):
        self.max = max # max level
        self.p = p
        self.head = Node(self.max, -1)
        self.level = 0

    def rand_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max:
            lvl += 1
        return lvl

    def delete(self, key):
        update = [None]*(self.max+1)
        node = self.head
        for level in range(self.level, -1, -1):
            while node.forward[level] and node.forward[level].key < key:
                node = node.forward[level]
            update[level] = node

        node = node.forward[0]

        if node and node.key == key:
            for lvl in range(self.level+1):
                if update[lvl].forward[lvl] != node:
                    break
                update[lvl].forward[lvl] = node.forward[lvl]

            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1

    def insert(self, key):
        update = [None]*(self.max+1)
        node = self.head
        for i in range(self.level, -1, -1):
            while node.forward[i] and node.forward[i].key < key:
                node = node.forward[i]
            update[i] = node

        node = node.forward[0]

        if not node or node.key != key:
            rand_level = self.rand_level
            if rand_level > self.level:
                for i in range(self.level, rand_level+1):
                    update.append(self.head)
                self.level = rand_level

            new_node = Node(key, rand_level)
            for lvl in range(rand_level+1):
                new_node.forward[0] = update[lvl].forward[0]
                update[lvl].forward[0] = new_node


    def search(self, key):
        node = self.head
        for l in range(self.max, -1, -1):
            while node.forward[l] and node.forward[l].key < key:
                node = node.forward[l]
        if node and node.key == key:
            return node
        return None

    def print(self):
        node = self.head
        for l in range(self.max):
            print(f"{l} level")
            node = node.forward[l]
            while node:
                print(node.key, end=" ")
                node = node.forward[l]
            print("")
