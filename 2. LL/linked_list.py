"""
Filename: linked_list.py
Desription: Creates and manages a linked list
Author: Priyankar Shivhare
Date: April 1, 2025
"""

class Node:
    """
    Creates a new Node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Instantiate a LinkedList
    """
    def __init__(self, value = None):
        if value is not None:
            self.head = self.tail = Node(value)
            self.length = 1
        else:
            self.head = self.tail = None
            self.length = 0

    def print_list(self):
        """
        Prints the Linked List
        """
        temp = self.head
        print ("Start ->", end=" ")

        while temp is not None:
            print(f"{temp.value} ->", end=" ")
            temp = temp.next
        print ("End")
        print (f"Head:{self.head.value if self.head else None} " +
               f"Tail:{self.tail.value if self.tail else None} " +
               f"Length:{self.length}", end="\n\n")

    def append(self, value):
        """
        Appends the new node at the end
        """
        new_node = Node(value=value)
        if self.length == 0:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        Pops the last node from the LL
        """
        if self.length == 0:
            return None
        if self.length == 1:
            ret_val = self.head
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            ret_val = temp.next
            self.tail = temp
            self.tail.next = None
        self.length -= 1
        return ret_val

    def prepend(self,value):
        """
        Prepends a new node
        """
        new_node =  Node(value=value)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
        return True

    def pop_first(self):
        """
        Pops the first element
        """
        if self.length == 0:
            return None
        if self.length == 1:
            ret_val = self.head
            self.head = self.tail = None
        else:
            ret_val = self.head
            self.head = self.head.next
        self.length -= 1
        return ret_val

    def get(self, index):
        """
        Gets the value at the given index
        """
        if index < 0 or index > self.length - 1:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        """
        Sets the value at the given index
        """
        temp = self.get(index=index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Inserts a new node at the given index
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value=value)
        prev_node = self.get(index = index - 1)
        new_node.next =  prev_node.next
        prev_node.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        Removes a node at the given index
        """
        if index < 0 or index > self.length - 1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev_node = self.get(index = index - 1)
        node = prev_node.next
        prev_node.next = node.next
        node.next = None
        self.length -= 1
        return node

    def reverse(self):
        """
        Reverses a LL
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
