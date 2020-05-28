#Perfect Number - Burak Karabey

def perfect_number(input_number):
    number = 1
    perfect_number = []
    while number <= input_number:
        divider = [s for s in range(1, number) if number % s == 0]
        i = 0
        total = 0
        while i < len(divider):
            total = total + divider[i]
            i += 1
        if number == total:
            perfect_number.append(number)
        number += 1
    return perfect_number

#USAGE
input = int(input("Enter the number for max range:"))
print("Perfect numbers in entered range =", perfect_number(input))
