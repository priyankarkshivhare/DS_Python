"""
Filename: heap_test.py
Desription: Tests the MaxHeap code
Author: Priyankar Shivhare
Date: April 23, 2025
"""
from heap import MaxHeap, MinHeap

def test_max_heap():
    """Test Heaps Functionality"""
    print("Testing Max Heap:")
    try:
        my_heap = MaxHeap() # Test Construtor
        assert not my_heap.heap
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        my_heap.insert(99) # Test Simple Insert 
        my_heap.insert(72)
        my_heap.insert(61)
        my_heap.insert(58)
        assert my_heap.heap == [99, 72, 61, 58]
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        my_heap.insert(100) # Insert at Top
        assert my_heap.heap == [100, 99, 61, 58, 72]
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        my_heap.insert(75) # Insert in between
        assert my_heap.heap == [100, 99, 75, 58, 72, 61]
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        my_heap.remove() # Remove the max
        assert my_heap.heap == [99, 72, 75, 58, 61]
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        my_heap = MaxHeap() # Start Fresh
        my_heap.insert(95) # Test Simple Insert 
        my_heap.insert(75)
        my_heap.insert(80)
        my_heap.insert(55)
        my_heap.insert(60)
        my_heap.insert(50)
        my_heap.insert(65)
        assert my_heap.heap == [95, 75, 80, 55, 60, 50, 65]
        my_heap.remove()
        assert my_heap.heap == [80, 75, 65, 55, 60, 50]
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

def test_min_heap():
    """Test Heaps Functionality"""
    print("Testing Min Heap:")
    try:
        my_heap = MinHeap() # Test Construtor
        assert not my_heap.heap
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        my_heap.insert(99) # Test Simple Insert 
        my_heap.insert(72)
        my_heap.insert(61)
        my_heap.insert(58)
        assert my_heap.heap == [58, 61, 72, 99]
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        my_heap.insert(100) # Insert at Bottom
        assert my_heap.heap == [58, 61, 72, 99, 100]
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        my_heap.insert(75) # Insert in between
        assert my_heap.heap == [58, 61, 72, 99, 100, 75]
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        my_heap.remove() # Remove the min
        assert my_heap.heap == [61, 75, 72, 99, 100]
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        my_heap = MinHeap() # Start Fresh
        my_heap.insert(95) # Test Simple Insert 
        my_heap.insert(75)
        my_heap.insert(80)
        my_heap.insert(55)
        my_heap.insert(60)
        my_heap.insert(50)
        my_heap.insert(65)
        assert my_heap.heap == [50, 60, 55, 95, 75, 80, 65]
        my_heap.remove()
        assert my_heap.heap == [55, 60, 65, 95, 75, 80]
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

test_max_heap()
test_min_heap()
