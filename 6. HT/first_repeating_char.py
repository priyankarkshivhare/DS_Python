"""
Write a function called first_non_repeating_char(string) that finds
the first non-repeating character in the given string using a hash
table (dictionary). If there is no non-repeating character in the
string, the function should return None.

For example, if the input string is "leetcode", the function should 
return "l" because "l" is the first character that appears only 
once in the string. Similarly, if the input string is "hello", 
the function should return "h" because "h" is the first non-repeating
character in the string.

    EXPECTED OUTPUT:
    ----------------
    l
    h
    None
"""
def first_non_repeating_char(my_string):
    """Finds first non repeating haracter"""
    my_dict = {}
    for char in my_string:
        if char in my_dict:
            my_dict[char] = True
        else:
            my_dict[char] = False
    ret_val = None
    for key, value in my_dict.items():
        if value is False:
            ret_val = key
            break
    return ret_val


print( first_non_repeating_char('leetcode') )
print( first_non_repeating_char('hello') )
print( first_non_repeating_char('aabbcc') )

