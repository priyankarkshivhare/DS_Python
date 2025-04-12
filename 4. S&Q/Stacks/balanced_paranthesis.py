"""
Stack: Parentheses Balanced ( ** Interview Question)
Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there
is a matching closing parenthesis in the correct order. 
For example, the string "((()))" has three pairs of balanced 
parentheses, so it is a balanced string. On the other hand, 
the string "(()))" has an imbalance, as the last two parentheses 
do not match, so it is not balanced.  Also, the string ")(" is 
not balanced because the close parenthesis needs to follow 
the open parenthesis.

Your program should take a string of parentheses as input 
and return True if it is balanced, or False if it is not. 
In order to solve this problem, use a Stack data structure.

Function name:
is_balanced_parentheses

The reverse_string function takes a single parameter string,
 which is the string you want to reverse.

Return a new string with the letters in reverse order.

Function name:
reverse_string

"""

class Stack:
    """Stack Class"""
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        """Prints Stack"""
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        """Check if is Empty"""
        return len(self.stack_list) == 0

    def peek(self):
        """Peeks the Value of the stack"""
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        """Returns Size of the Stack"""
        return len(self.stack_list)

    def push(self, value):
        """Push"""
        self.stack_list.append(value)

    def pop(self):
        """Pop"""
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def is_balanced_parentheses(string):
    """Return True of false as per description"""
    my_stack = Stack()
    for index in range(len(string)):
        my_stack.push(string[len(string)-index-1])
    is_balanced = 0
    popped_val = my_stack.pop()
    while(popped_val):
        if popped_val == "(":
            is_balanced += 1
        elif popped_val == ")":
            is_balanced -= 1
        if is_balanced < 0:
            return False
        popped_val = my_stack.pop()
    if is_balanced == 0:
        return True
    return False

def reverse_string(string):
    pass
# WRITE IS_BALANCED_PARENTHESES FUNCTION HERE #
#                                             #
#    This is a separate function that is      #
#    not a method within the Stack class.     #
#    Indent all the way to the left.          #
#                                             #
###############################################




def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

def test_reverse_string():
    try:
        my_string = 'hello'

        assert reverse_string(my_string) == "olleh"
        print('Test case 12 passed')
    except AssertionError:
        print('Test case 12 failed')

test_is_balanced_parentheses()
# is_balanced_parentheses("((()))")
test_reverse_string()
