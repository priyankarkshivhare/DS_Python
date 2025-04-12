"""
Filename: stack_test.py
Desription: Tests the stack code
Author: Priyankar Shivhare
Date: April 12, 2025
"""
from stack import Stack

def stack_as_list(stack):
    """
    Returns stack as list
    """
    # Collect values from the stack and compare
    result_values = []
    node = stack.top
    while node:
        result_values.append(node.value)
        node = node.next
    return result_values

def test_all_functions():
    """Test Stack Functionality"""
    try:
        my_stack = Stack(1)
        assert stack_as_list(my_stack) == [1]
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        my_stack = Stack(1)
        my_stack.push(2)
        my_stack.push(3)
        my_stack.push(4)
        assert stack_as_list(my_stack) == [4, 3, 2, 1]
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        my_stack = Stack()
        my_stack.push(2)
        my_stack.push(3)
        my_stack.push(4)
        assert stack_as_list(my_stack) == [4, 3, 2]
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert my_stack.pop().value == 4
        assert stack_as_list(my_stack) == [3, 2]
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        my_stack.pop()
        my_stack.pop()
        my_stack.pop()
        my_stack.pop()
        assert stack_as_list(my_stack) == []
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

test_all_functions()
