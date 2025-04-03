"""
You are given a singly linked list and two integers start_index and end_index.
Your task is to write a method reverse_between within the LinkedList class 
that reverses the nodes of the linked list from start_index to 
end_index (inclusive using 0-based indexing) in one pass and in-place.

Assumption: You can assume that start_index and end_index are not out of bounds.

Input
The method reverse_between takes two integer inputs start_index and end_index.
The method will only be passed valid indexes 

Output
The method should modify the linked list in-place 
by reversing the nodes from start_index to  end_index.

If the linked list is empty or has only one node, 
the method should return None.

Example
Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, 
and start_index = 2 and end_index = 4. 
Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        if self.length < 2:
            print("BP0")
            return None
        before = before_node = start_node = end_node = after_node = None
        temp = self.head
        for i in range(self.length):
            if i == start_index - 1:
                before_node = temp
            if i == start_index:
                start_node = temp
            if i == end_index:
                end_node = temp
            if i == end_index + 1:
                after_node = temp

            after = temp.next

            if i >= start_index and i <= end_index:
                temp.next = before
                before = temp
            temp = after
        if before_node is not None:
            before_node.next = end_node
        else: 
            self.head = end_node
        if after_node is not None:
            start_node.next = after_node

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
