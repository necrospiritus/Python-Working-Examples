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


def divide_by_2(dec_number):
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


print(divide_by_2(196))
