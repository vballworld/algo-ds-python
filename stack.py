"""
a linkedlist-based stack implementation in Python
"""

from linkedlist import *


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        if self.top is not None:
            n = Node(val)
            n.next = self.top
            self.top = n
        else:
            self.top = Node(val)

        self.size += 1

    def pop(self):
        if self.top is not None:
            prev_top = self.top
            self.top = prev_top.next
            self.size -= 1
            return prev_top.val
        else:
            print("stack is empty.")
            return None

    def print(self):
        n = self.top
        while n is not None:
            print("{0}->".format(n.val), end="")
            n = n.next
        print("None")

    def get_size(self):
        return self.size

    def get_top(self):
        if self.top is not None:
            return self.top.val
        else:
            print("stack is empty.")
            return None


s1 = Stack()
s1.print()
s1.push(5)
s1.push(8)
s1.push(2)
s1.print()
print(s1.get_size())
print(s1.pop())
print(s1.get_top())