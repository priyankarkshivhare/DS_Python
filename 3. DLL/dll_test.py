"""
Filename: dll_test.py
Desription: Tests the doubly linked list code
Author: Priyankar Shivhare
Date: April 1, 2025
"""
from dll import DoublyLinkedList

# my_dll = DoublyLinkedList(4)
# my_dll.print_list()
# my_dll.append(3)
# my_dll.print_list()
# print(my_dll.pop().value)
# my_dll.print_list()

# new_linked_list = DoublyLinkedList()
# new_linked_list.print_list()
# print(new_linked_list.pop())
# new_linked_list.print_list()
# new_linked_list.append(3)
# new_linked_list.print_list()
# print(new_linked_list.pop().value)
# new_linked_list.print_list()
# new_linked_list.prepend(4)
# new_linked_list.print_list()
# new_linked_list.prepend(3)
# new_linked_list.print_list()
# new_linked_list.prepend(2)
# new_linked_list.print_list()
# print((new_linked_list.get(0)).value)
# print((new_linked_list.get(1)).value)
# print((new_linked_list.get(2)).value)

# print(new_linked_list.set(0, 5))
# print(new_linked_list.set(1, 6))
# print(new_linked_list.set(2, 7))
# new_linked_list.print_list()

# print(new_linked_list.insert(3, 4))
# print(new_linked_list.insert(0, 3))
# print(new_linked_list.insert(3, 2))
# new_linked_list.print_list()




# print(new_linked_list.pop_first())
# new_linked_list.print_list()
# print(new_linked_list.pop_first())
# new_linked_list.print_list()
# print(new_linked_list.pop_first())
# new_linked_list.print_list()
# print(new_linked_list.pop_first())
# new_linked_list.print_list()

# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.append(4)
# my_doubly_linked_list.append(5)


# print('DLL before reverse():')
# my_doubly_linked_list.print_list()


# my_doubly_linked_list.reverse()


# print('\nDLL after reverse():')
# my_doubly_linked_list.print_list()

my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )
