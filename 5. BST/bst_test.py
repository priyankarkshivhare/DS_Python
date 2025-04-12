"""
Filename: bst_test.py
Desription: Tests the BST code
Author: Priyankar Shivhare
Date: April 12, 2025
"""
from bst import BinarySearchTree


def test_all_functions():
    """Test Stack Functionality"""
    try:
        my_bst = BinarySearchTree() # Test Construtor
        assert my_bst.root is None
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert my_bst.insert(4) is True # Test Inserting Root Node
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')


    try:
        assert my_bst.insert(3) is True # Test Inserting Left Node
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert my_bst.insert(5) is True # Test Inserting Right Node
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert my_bst.insert(6) is True # Test Inserting Right Node -Second Level
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert my_bst.insert(6) is False # Test Inserting duplicate nodes
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert my_bst.contains(6) is True # Test contains True case
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert my_bst.contains(4) is True # Test Root Node True case
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert my_bst.contains(7) is False # Test contains False case
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        my_bst = BinarySearchTree() # Test Construtor

        assert my_bst.contains(7) is False # Test empty BST case
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

test_all_functions()
