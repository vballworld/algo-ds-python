"""
a list-based stack implementation in Python
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("stack is empty.")
            return None

    def print(self):
        print("bottom", end="")
        print(self.stack, end="")
        print("top")

    def get_size(self):
        return len(self.stack)

    def get_top(self):
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

# s1 = Stack()
# s1.print()
# s1.push(5)
# s1.push(8)
# s1.push(2)
# print(s1.is_empty())
#
# s1.print()
# print(s1.get_size())
# print(s1.pop())
# s1.print()
# s1.pop()
# s1.pop()
# s1.pop()
#
# print(s1.is_empty())
# s1.pop()
# s1.print()