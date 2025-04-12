"""
Stack: Implement Stack Using a List ( ** Interview Question)
In the Stack: Intro video we discussed how stacks are commonly 
implemented using a list instead of a linked list.

1. Create a constructor for Class Stack that implements a new 
   stack with an empty list called stack_list
2. Add a method to push a value onto the Stack implementation 
   that we began in the last Coding Exercise.
3. Add a method to pop a value
"""
class Stack:
    """
    Stack using Python List
    """
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        """
        Prints Stack Content
        """
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def push(self, value):
        """
        Pushes Data into the stack
        """
        self.stack_list.append(value)

    def pop(self):
        """
        Pops data from the stack
        """
        if self.stack_list:
            return self.stack_list.pop(-1)

def test_code(stack, expected):
    """ Test Codes"""
    print(f"TEST: {stack.stack_list == expected}")

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

test_code(my_stack,[1, 2, 3])
my_stack.print_stack()

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop())

print("\nStack after pop():")
my_stack.print_stack()
test_code(my_stack,[1, 2])
