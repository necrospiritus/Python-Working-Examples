"""A stack is an ordered collection of items where the addition of new items and removal of existing items
always takes place at the same end. This end is commonly referred to as the 'top'.
The end opposite the top is known as the 'base'."""


# Completed implementation of a stack ADT
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):  # test to see whether the stack is empty.
        return self.items == []

    def push(self, item):  # adds a new item to the top of the stack.
        self.items.append(item)

    def pop(self):  # removes the top item from the stack.
        return self.items.pop()

    def peek(self):  # return the top item from the stack.
        return self.items[len(self.items) - 1]

    def size(self):  # returns the number of items on the stack.
        return len(self.items)

s = Stack()

print(s.is_empty())
s.push(4)
s.push("Dog")
print(s.peek())
s.push("Cat")
print(s.size())
print(s.is_empty())
s.pop()
print(s.peek())
print(s.size())
