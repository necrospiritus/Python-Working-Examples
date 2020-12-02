"""Reverse stack is using a list where the top is at the beginning instead of at the end."""


class Reverse_Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):  # test to see whether the stack is empty.
        return self.items == []

    def push(self, item):  # adds a new item to the base of the stack.
        self.items.insert(0, item)

    def pop(self):  # removes the base item from the stack.
        return self.items.pop(0)

    def peek(self):  # return the base item from the stack.
        return self.items[0]

    def size(self):  # returns the number of items on the stack.
        return len(self.items)


s = Reverse_Stack()

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
