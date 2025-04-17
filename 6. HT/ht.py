"""
Filename: ht.py
Desription: Creates and manages a Hash Table
Author: Priyankar Shivhare
Date: April 17, 2025
"""

# GLobal Variables
DEFAULT_SIZE = 7
HASH_SEED = 23

class HashTable:
    """
    Instantiate a HT
    """
    def __init__(self, size = DEFAULT_SIZE):
        self.data_map = [None] * size

    def __hash(self, keys):
        my_hash = 0
        for letter in keys:
            my_hash = (my_hash + ord(letter) * HASH_SEED) % len(self.data_map)
        return my_hash

    def print_ht(self):
        """
        Prints the Hash Table
        """
        for i, val in enumerate(self.data_map):
            print(i, " : ", val)

    def set_item(self, key, value):
        """Sets the item in hash table"""
        index = self.__hash(keys=key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """Gets the item with the key"""
        index = self.__hash(keys=key)
        for items in self.data_map[index]:
            if key == items[0]:
                return items[1]
        return None

    def keys(self):
        """Gets all the keys as a list"""
        all_keys = []
        for _, val in enumerate(self.data_map):
            if val is not None:
                for item in val:
                    all_keys.append(item[0])
        return all_keys
