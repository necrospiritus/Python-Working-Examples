# Greatest Common Divisor - Burak Karabey

def GCD(x, y):
    x_divisor = [s1 for s1 in range(1, x+1) if x % s1 == 0]
    y_divisor = [s2 for s2 in range(1, y+1) if y % s2 == 0]
    common_divisors = x_divisor + y_divisor
    common_divisors.sort()
    i = 0
    greatest_common_divisor = []
    while i < len(common_divisors):
        j = i + 1
        while j < len(common_divisors):
            if common_divisors[i] == common_divisors[j]:
                greatest_common_divisor.append(common_divisors[i])
                break
            else:
                j += 1
        i += 1
    greatest_common_divisor.sort(reverse=True)

    return print("GCD=", greatest_common_divisor[0])

# USAGE
GCD(54,24)
