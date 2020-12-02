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


# Completed extended par_checker for: [,{,(,),},]

def matches(open, close):
    opens = "{[("
    closes = "}])"
    return opens.index(open) == closes.index(close)


def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False


print(par_checker('((()))'))
print(par_checker('(()'))
print(par_checker("[{()]"))
