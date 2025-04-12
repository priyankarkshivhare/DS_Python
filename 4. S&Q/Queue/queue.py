"""
Filename: queue.py
Desription: Creates and manages a Queue
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

class Queue:
    """
    Instantiate a Queue
    """
    def __init__(self, value = None):
        if value is not None:
            self.first = self.last = Node(value)
            self.length = 1
        else:
            self.first = self.last = None
            self.length = 0

    def print_list(self):
        """
        Prints the Linked List
        """
        temp = self.first
        print ("Start ->", end=" ")

        while temp is not None:
            print(f"{temp.value} ->", end=" ")
            temp = temp.next
        print ("End")
        print (f"Head:{self.first.value if self.first else None} " +
               f"Length:{self.length}", end="\n\n")

    def enqueue(self, value):
        """
        Pushes data in the stack
        """
        new_node = Node(value=value)
        if self.length != 0:
            self.last.next = new_node
            self.last = new_node
        else:
            self.first = self.last = new_node
        self.length += 1

    def dequeue(self):
        """
        Pops the data from the node
        """
        if self.length == 0:
            return None
        ret_val = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = ret_val.next
            ret_val.next = None
        self.length -= 1
        return ret_val
