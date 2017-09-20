"""
a linkedlist-based stack implementation in Python
"""

from linkedlist import *


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        if self.top is None:
            self.top = Node(val)
        else:
            n = Node(val)
            n.next = self.top
            self.top = n

        self.size += 1

    def pop(self):
        if self.top is None:
            print("stack is empty.")
            return None
        else:
            prev_top = self.top
            self.top = prev_top.next
            self.size -= 1
            return prev_top.val

    def print(self):
        n = self.top
        while n is not None:
            print("{0}->".format(n.val), end="")
            n = n.next
        print("None")


# s1 = Stack()
# s1.print()
# 
# s1.push(5)
# s1.push(8)
# s1.push(2)
# s1.print()
# 
# print(s1.pop())
# s1.print()