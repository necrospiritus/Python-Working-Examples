import random


def generate_sentence():
    alphabet = "abcdefghijklmnoprstuvyzqwx "
    sentence = ""
    i = 0
    while i <= 27:
        sentence = sentence + alphabet[random.randint(0, 26)]
        i += 1
    return sentence


def calculate_score():
    sentence = generate_sentence()
    correct_sentence = "methinks it is like a weasel"
    score = 0
    for i, j in zip(sentence, correct_sentence):
        if i == j:
            score = score + 1
        else:
            pass
    return score, sentence


def find_best_match():
    k = 0
    max_score = 0
    best_sentence = ""
    while True:
        score, sentence = calculate_score()
        if score == 27:
            print(k, ".try")
            print(sentence)
            print("Score= %", (score * 100) // 27)
            break
        else:
            if score > max_score:
                best_sentence = sentence
                max_score = score
            if (k % 10000) == 0:
                print(k, ".try")
                print(best_sentence, " Score= %", (max_score * 100) // 27, "\n")
            k += 1


find_best_match()
