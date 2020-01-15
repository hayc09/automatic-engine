#!/usr/bin/env python3


def letter_count(x, y):
    """ Function takes a word and a letter, turns to upper case, then looks
    for the number of times it shows up """
    word = x.upper()
    char = y.upper()
    number = 0
    for letter in word:
        if letter == char:
            number += 1
        else:
            number += 0

    return print("The letter " + char + " show's up " + str(number) + " times in the word " + word)


if __name__ == "__main__":
    letter_count('banana', 'a')
    letter_count('banana', 'n')
    letter_count('banana', 'x')








