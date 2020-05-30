
#Factorial Function - Burak Karabey

def factorial_function():
    number = int(input("Enter the number: "))
    i = 1
    factorial = 1
    while i <= number:
        factorial = factorial * i
        i += 1
    return print("{}! = {}".format(number, factorial))

#USAGE
factorial_function()
