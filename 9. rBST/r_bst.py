"""
Filename: bst.py
Desription: Creates and manages a Binary Search Tree
Author: Priyankar Shivhare
Date: April 12, 2025
"""

class Node:
    """
    Creates a new Node for BST
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Instantiate a BST
    """
    def __init__(self):
        self.root = None

    def __r_insert(self, value, node):
        """
        Recursive Insert
        """
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.__r_insert(value = value, node = node.left)
        if value > node.value:
            node.right = self.__r_insert(value = value, node = node.right)
        return node

    def __r_contains(self,value, node):
        """Recursive Contains"""
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self.__r_contains(value=value,node=node.left)
        return self.__r_contains(value=value,node=node.right)

    def insert(self, value):
        """
        Inserts a new node in BST
        """
        if self.root is None:
            self.root = Node(value)
        return self.__r_insert(value=value, node=self.root)

    def contains(self, value):
        """
        Checks if the BST contains the given value
        """
        return self.__r_contains(value=value, node=self.root)

    def __r_delete(self, value, node):
        """Deletes a node from BST"""
        if node is None:
            return None
        if value < node.value: # Travel Left
            node.left = self.__r_delete(value=value, node=node.left)
        elif value > node.value: # Travel Right
            node.right = self.__r_delete(value=value, node=node.right)
        else: # Delete this node
            if node.left is None and node.right is None: # Corner Node
                return None
            if node.left is None: # Nodes on Left Only
                return node.right
            if node.right is None: # Nodes on right Only
                return node.left
            min_val = self.sub_tree_min(node=node.right)
            node.value = min_val
            node.right = self.__r_delete(value=min_val, node=node.right)
        return node

    def sub_tree_min(self, node):
        """Finds and return a min value from any tree or sub-tree"""
        while node.left is not None:
            node = node.left
        return node.value

    def delete(self, value):
        """Deletes a Node from BST"""
        self.__r_delete(value=value, node=self.root)
