# Pythagorean Triple - Burak Karabey

def triangle(input_number):
    list_of_numbers = [i for i in range(1, input_number+1)]
    pythagorean_triple = []
    for j in list_of_numbers:
        for k in list_of_numbers:
            c = (j ** 2 + k ** 2) ** 0.5
            if c == int(c):
                pythagorean_triple.append((j, k, int(c)))
    return print("Pythagorean Triples =", pythagorean_triple)

#USAGE
triangle(10)
