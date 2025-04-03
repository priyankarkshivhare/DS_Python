"""
Filename: linked_list_test.py
Desription: Tests the linked list code
Author: Priyankar Shivhare
Date: April 1, 2025
"""
from linked_list import LinkedList

my_linked_list = LinkedList(4)
my_linked_list.print_list()
my_linked_list.append(3)
my_linked_list.print_list()
print(my_linked_list.pop().value)
my_linked_list.print_list()
new_linked_list = LinkedList()
new_linked_list.print_list()
print(new_linked_list.pop())
new_linked_list.print_list()
new_linked_list.append(3)
new_linked_list.print_list()
print(new_linked_list.pop().value)
new_linked_list.print_list()
new_linked_list.prepend(4)
new_linked_list.print_list()
new_linked_list.prepend(3)
new_linked_list.print_list()
new_linked_list.prepend(2)
new_linked_list.print_list()
print(new_linked_list.get(0))
print(new_linked_list.get(1))
print(new_linked_list.get(2))

print(new_linked_list.set(0, 5))
print(new_linked_list.set(1, 6))
print(new_linked_list.set(2, 7))
new_linked_list.print_list()

print(new_linked_list.insert(3, 4))
print(new_linked_list.insert(0, 3))
print(new_linked_list.insert(3, 2))
new_linked_list.print_list()

new_linked_list.reverse()
new_linked_list.print_list()

print(new_linked_list.remove(5))
print(new_linked_list.remove(0))
print(new_linked_list.remove(3))
new_linked_list.print_list()

print(new_linked_list.pop_first())
new_linked_list.print_list()
print(new_linked_list.pop_first())
new_linked_list.print_list()
print(new_linked_list.pop_first())
new_linked_list.print_list()
print(new_linked_list.pop_first())
new_linked_list.print_list()
