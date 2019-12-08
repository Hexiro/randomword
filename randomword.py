import json
import random

words = json.loads(open("words_dictionary.json").read())


def get_random_word(amount=1):
    try:
        int(amount)
    except ValueError:
        exit(f"ValueError: '{amount}' is not an integer. (integer ex. 1, 3, 15, etc.)")
    try:
        if int(amount) is 0:
            exit("'0' Is not an excepted field. Please use a number 1 and above.")
        if int(amount) is 1:
            a_random_word = random.choice(words)
            return a_random_word
        if int(amount) >= 2:
            multiple_random_words = random.sample(words, amount)
            return multiple_random_words
    except TypeError:
        exit(f"TypeError: can't multiply sequence by non-integer {amount}. (integer ex. 1, 6, 32, etc.)")
