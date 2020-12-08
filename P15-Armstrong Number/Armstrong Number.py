# Armstrong Number - Burak Karabey
def armstrong(x):
    input_number = list(str(x))
    i = 0
    u = 0
    while i < len(input_number):
        u = u + (int(input_number[i]) ** len(input_number))
        i += 1
    u = str(u)
    armstrong_number = []
    for n in range(0, len(u)):
        armstrong_number.append(u[n])

    if input_number == armstrong_number:
        print("This is an Armstrong Number!")
    else:
        print("This is NOT an Armstrong Number!")

#USAGE
armstrong(6)
