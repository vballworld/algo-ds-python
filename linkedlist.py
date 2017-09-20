class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def add_to_head(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def print(self):
        node = self.head

        if node is None:
            print("list is empty.")

        while node is not None:
            print("{0}->".format(node.val), end="")
            node = node.next
        print("None")

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False


n1 = Node(3)
n2 = Node(5)
n3 = Node(9)

l1 = LinkedList()

l2 = LinkedList(n1)
l2.add_to_head(n2)
l2.add_to_head(n3)
l2.print()

print(l2.is_empty())
print(l1.is_empty())