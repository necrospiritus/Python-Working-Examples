# Least Common Multiple (LCM) Calculator - Burak Karabey

def LCM(x, y):
    if x > y:
        limit = x
    else:
        limit = y
    prime_numbers = []  # Start of Finding Prime Number
    if limit < 2:
        return prime_numbers.append(0)
    elif limit == 2:
        return prime_numbers.append(2)
    else:
        prime_numbers.append(2)
        for t in range(3, limit):
            find_prime = False
            for r in range(2, t):
                if t % r == 0:
                    find_prime = True
                    break
            if not find_prime:
                prime_numbers.append(t)
    prime_numbers.sort()  # End of Finding Prime Number
    i = 0
    least_common_multiple = 1
    while x != 1 or y != 1:
        if x % prime_numbers[i] == 0 or y % prime_numbers[i] == 0:
            least_common_multiple = least_common_multiple * prime_numbers[i]
            if x % prime_numbers[i] == 0:
                x = x / prime_numbers[i]
            if y % prime_numbers[i] == 0:
                y = y / prime_numbers[i]
        else:
            i += 1

    return print("LCM=", least_common_multiple)

# USAGE
LCM(12,15)
