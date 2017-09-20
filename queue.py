"""
a list-based queue implementation in Python
"""

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, val):
        self.queue.insert(0, val)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            print("stack is empty.")
            return None

    def print(self):
        print("end", end="")
        print(self.queue, end="")
        print("start")

    def get_size(self):
        return len(self.queue)

    def get_top(self):
        return self.queue[len(self.queue) - 1]

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

q1 = Queue()
q1.print()

q1.push(1)
q1.push(2)
q1.push(3)
q1.print()

q1.pop()
q1.print()

q1.pop()
q1.print()

q1.pop()
q1.pop()
