"""
Filename: queue_test.py
Desription: Tests the queue code
Author: Priyankar Shivhare
Date: April 12, 2025
"""
from queue import Queue

def queue_as_list(queue):
    """
    Returns queue as list
    """
    # Collect values from the stack and compare
    result_values = []
    node = queue.first
    while node:
        result_values.append(node.value)
        node = node.next
    return result_values

def test_all_functions():
    """Test Stack Functionality"""
    try:
        my_queue = Queue(1)
        assert queue_as_list(my_queue) == [1]
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        my_queue = Queue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        my_queue.enqueue(4)
        assert queue_as_list(my_queue) == [1, 2, 3, 4]
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        my_queue = Queue()
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        my_queue.enqueue(4)
        assert queue_as_list(my_queue) == [2, 3, 4]
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert my_queue.dequeue().value == 2
        assert queue_as_list(my_queue) == [3, 4]
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        my_queue.dequeue()
        my_queue.dequeue()
        my_queue.dequeue()
        my_queue.dequeue()
        assert queue_as_list(my_queue) == []
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

test_all_functions()