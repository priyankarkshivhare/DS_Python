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

    def insert(self, value):
        """
        Inserts a new node in BST
        """
        new_node =  Node(value=value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if value == temp.value:
                return False
            if value < temp.value: # Value is less than current node, travel Left
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        """
        Checks if the BST contains the given value
        """
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            if value <= temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False
