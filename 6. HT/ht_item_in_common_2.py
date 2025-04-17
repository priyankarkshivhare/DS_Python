"""
Write a function item_in_common(list1, list2) that takes two lists as
input and returns True if there is at least one common item between
the two lists, False otherwise.

Use a dictionary to solve the problem that creates an O(n) time complexity.
"""
def item_in_common(list1, list2):
    """ Returns TRUE if two list have something in common"""
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True

    return False


LIST1 = [1,3,5]
LIST2 = [2,4,6]


print(item_in_common(LIST1, LIST2))
