import timeit
from timeit import Timer


def t1(n):
    for i in range(n):
        for j in range(n):
            k = 2 + n
    return k


timer1 = Timer("t1(100)", "from __main__ import t1")
print("Function Time= ", timer1.timeit(number=1000), "milliseconds")
