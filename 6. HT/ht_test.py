"""
Filename: ht_test.py
Desription: Tests the HT code
Author: Priyankar Shivhare
Date: April 17, 2025
"""
from ht import HashTable

def test_all_functions():
    """Test Hash Table Functionality"""
    try:
        my_ht = HashTable() # Test Construtor
        assert my_ht.data_map == [None, None, None, None, None, None, None]
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        my_ht.set_item('bolts', 1400) # Test set item
        my_ht.set_item('washers', 50)
        my_ht.set_item('lumber', 70)
        expected_data_map = [
            None,
            None,
            None,
            None,
            [['bolts', 1400], ['washers', 50]],
            None,
            [['lumber', 70]]
        ]
        assert my_ht.data_map == expected_data_map
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')


    try:
        assert my_ht.get_item('lumber') == 70 # Test getting a value which exists
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert my_ht.get_item('nuts') is None # Test getting a value which doesn't exist
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert my_ht.keys() == ['bolts', 'washers', 'lumber'] # Test keys method
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

test_all_functions()
