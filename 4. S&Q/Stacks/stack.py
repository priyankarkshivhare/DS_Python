"""
Filename: stack.py
Desription: Creates and manages a Stack
Author: Priyankar Shivhare
Date: April 12, 2025
"""

class Node:
    """
    Creates a new Node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """
    Instantiate a Stack
    """
    def __init__(self, value = None):
        if value is not None:
            self.top = Node(value)
            self.height = 1
        else:
            self.top = None
            self.height = 0

    def print_list(self):
        """
        Prints the Linked List
        """
        temp = self.top
        print ("Start ->", end=" ")

        while temp is not None:
            print(f"{temp.value} ->", end=" ")
            temp = temp.next
        print ("End")
        print (f"Head:{self.top.value if self.top else None} " +
               f"Length:{self.height}", end="\n\n")

    def push(self, value):
        """
        Pushes data in the stack
        """
        new_node = Node(value=value)
        if self.top:
            new_node.next = self.top

        self.top = new_node
        self.height += 1

    def pop(self):
        """
        Pops the data from the node
        """
        ret_val = None
        if self.top:
            ret_val = self.top
            self.top = ret_val.next
            ret_val.next = None
            self.height -= 1
        return ret_val
