"""
Filename: bst_test.py
Desription: Tests the BST code
Author: Priyankar Shivhare
Date: April 12, 2025
"""
from r_bst import BinarySearchTree

def test_all_functions():
    """Test Recursive BST Functionality"""
    try:
        my_bst = BinarySearchTree()
        my_bst.insert(47)
        my_bst.insert(21)
        my_bst.insert(76)
        my_bst.insert(18)
        my_bst.insert(27)
        my_bst.insert(52)
        my_bst.insert(82)
        assert my_bst.contains(27) is True # Test Recursive contains
        assert my_bst.contains(17) is False # Test Recursive contains
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        my_bst = BinarySearchTree() # Test Construtor
        my_bst.insert(47)
        assert my_bst.root.value == 47
        my_bst.insert(21)
        assert my_bst.root.left.value == 21
        my_bst.insert(76)
        assert my_bst.root.right.value == 76
        my_bst.insert(18)
        assert my_bst.root.left.left.value == 18
        my_bst.insert(27)
        assert my_bst.root.left.right.value == 27
        my_bst.insert(52)
        assert my_bst.root.right.left.value == 52
        my_bst.insert(82)
        assert my_bst.root.right.right.value == 82
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        my_bst = BinarySearchTree()
        my_bst.insert(47)
        my_bst.insert(21)
        my_bst.insert(76)
        my_bst.insert(18)
        my_bst.insert(27)
        my_bst.insert(52)
        my_bst.insert(82)
        my_bst.delete(27) # Test Delete Corner Node
        assert my_bst.contains(27) is False
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        my_bst.delete(21) # Test Delete Node with left branch
        assert my_bst.contains(21) is False
        assert my_bst.root.left.value == 18
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        my_bst = BinarySearchTree()
        my_bst.insert(47)
        my_bst.insert(21)
        my_bst.insert(76)
        my_bst.insert(18)
        my_bst.insert(27)
        my_bst.insert(52)
        my_bst.insert(82)
        my_bst.delete(18) # Test Delete Corner Node
        assert my_bst.contains(18) is False
        my_bst.delete(21) # Test Delete Node with right branch
        assert my_bst.contains(21) is False
        assert my_bst.root.left.value == 27
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        my_bst = BinarySearchTree()
        my_bst.delete(18) # Test Delete from empty Tree
        assert my_bst.root is None
        print("Test case 6 passed")
    except AssertionError:
        print("Test case 6 failed")

    try:
        my_bst = BinarySearchTree()
        my_bst.insert(47)
        my_bst.insert(21)
        my_bst.insert(76)
        my_bst.insert(18)
        my_bst.insert(27)
        my_bst.insert(52)
        my_bst.insert(82)
        my_bst.delete(100) # Test Delete non-existent Node
        assert my_bst.contains(100) is False
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(30)
        bst.insert(70)
        bst.insert(20)
        bst.insert(40)
        bst.insert(60)
        bst.insert(80)
        bst.insert(10)
        bst.insert(25)
        bst.insert(35)
        bst.insert(45)
        bst.insert(55)
        bst.insert(65)
        bst.insert(75)
        bst.insert(90)
        bst.delete(70) # Test Delete non-existent Node
        assert bst.contains(70) is False
        assert bst.root.right.value == 75
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

test_all_functions()
