"""
Filename: dll.py
Desription: Creates and manages a doubly linked list
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
        self.prev = None

class DoublyLinkedList:
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
            new_node.prev = self.tail
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
            temp = self.head
            self.head = self.tail = None
        else:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self,value):
        """
        Prepends a new node
        """
        new_node =  Node(value=value)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        """
        Pops the first element
        """
        if self.length == 0:
            return None
        ret_val = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            ret_val.next = None
        self.length -= 1
        return ret_val

    def get(self, index):
        """
        Gets the value at the given index
        """
        if index < 0 or index > self.length - 1:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1 - index):
                temp = temp.prev
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
        after_node = prev_node.next

        new_node.next =  after_node
        new_node.prev = prev_node

        prev_node.next = new_node
        after_node.prev = new_node
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
        after_node = node.next

        prev_node.next = after_node
        after_node.prev = prev_node

        node.next = None
        node.prev = None
        self.length -= 1
        return node

    def reverse(self):
        """
        Reverses a DLL
        """
        curr_node = self.head
        for _ in range(self.length):
            print(f"BP1: {curr_node.value}")
            temp = curr_node.prev
            curr_node.prev = curr_node.next
            curr_node.next = temp
            curr_node = curr_node.prev

        temp = self.head
        self.head = self.tail
        self.tail = temp

    def is_palindrome(self):
        """
        Checks whether DLL is Palindrome
        """
        start =self.head
        end = self.tail
        for _ in range(self.length//2):
            if start.value != end.value:
                return False
            start = start.next
            end = end.prev
        return True
