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


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string


print(base_converter(196, 2))
print(base_converter(25, 8))
print(base_converter(26, 16))