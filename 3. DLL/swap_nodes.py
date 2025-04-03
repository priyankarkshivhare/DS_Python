"""
You are given a doubly linked list.

Implement a method called swap_pairs within the class that swaps 
the values of adjacent nodes in the linked list. 
The method should not take any input parameters.

Example:
1 <-> 2 <-> 3 <-> 4 should become 2 <-> 1 <-> 4 <-> 3
Your implementation should handle edge cases such as an 
empty linked list or a linked list with only one node.

Note: You must solve the problem WITHOUT MODIFYING THE VALUES in the list's
nodes (i.e., only the nodes' prev and next pointers may be changed.)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        if self.length < 2:
            return
        new_head = self.head.next
        first_node = self.head
        for _ in range(self.length //2):
            second_node = first_node.next
            prev_node = first_node.prev
            after_node = second_node.next
            second_node.prev = prev_node
            second_node.next = first_node
            first_node.prev = second_node
            first_node.next = after_node
            if prev_node:
                prev_node.next = second_node
            if after_node:
                after_node.prev = first_node
            first_node = first_node.next

        self.head = new_head


my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""