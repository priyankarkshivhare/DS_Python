"""
find_duplicates()

Problem: Given an array of integers nums, find all the duplicates 
in the array using a hash table (dictionary).

Input:
A list of integers nums.

Output:
A list of integers representing the numbers in the input array nums
that appear more than once. If no duplicates are found in the input
array, return an empty list [].

    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

def find_duplicates(my_list):
    """ Finds and returns dupliates"""
    my_dict = {}
    for item in my_list:
        if item in my_dict:
            my_dict[item] = True
        else:
            my_dict[item] = False
    ret_val = []
    for key, value in my_dict.items():
        if value is True:
            ret_val.append(key)
    return ret_val

print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )
