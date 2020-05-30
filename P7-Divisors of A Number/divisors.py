# Divisors - Burak Karabey

def divisors(dividend, divisor):
    list_of_dividend = list()
    for i in range(1, dividend + 1):
        list_of_dividend.append(i)
    divisor_numbers = list()
    i = 0
    while i < dividend:
        remainder = list_of_dividend[i] % divisor
        i += 1
        if remainder != 0:
            continue
        divisor_numbers.append(list_of_dividend[i - 1])
    return print(divisor_numbers)


# USAGE
divisors(15, 4)
