"""
Filename: queue_test.py
Desription: Tests the queue code
Author: Priyankar Shivhare
Date: April 12, 2025
"""
from queue import Queue

def test_stack(test_name, queue, expected_values):
    """
    Test any Queue with the expected Values
    """
    # Collect values from the stack and compare
    result_values = []
    node = queue.first
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print(f"{test_name}:Test PASS")
    else:
        print(f"{test_name}:Test FAIL")
    print(f"Expected: {expected_values}")
    print(f"Result: {result_values}\n")


# Test 1: Constructor
my_queue = Queue(1)
test_stack("TEST_CONSTRUCTOR", my_queue, [1])

my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
test_stack("TEST_ENQUEUE", my_queue, [1, 2, 3, 4])

my_queue.dequeue()
test_stack("TEST_DEQUEUE", my_queue, [2, 3, 4])
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
test_stack("TEST_DEQUEUE", my_queue, [])
