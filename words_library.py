import random


def import_library():

    # Get liste_francais.txt and pass it throughout a Python list named library

    extract = open("liste_francais.txt")
    library = extract.readlines()

    library = list(map(lambda st: str.replace(st, "?", "e"), library))

    difficulty_list(library)


def difficulty_list(extracted_list):

    # divide list in 3 lists (easy, medium, hard)

    easy_list = []
    medium_list = []

    for word in extracted_list:
        if len(word) < 7:
            easy_list.extend([word])
            medium_list.extend([word])

        elif len(word) < 10:
            medium_list.extend([word])

    hard_list = extracted_list

    random_words_library(hard_list)


def random_words_library(difficulty_list):

    # give a random list from easy, medium or hard list

    random_word_list = []
    i = 0
    while i < 4:

        i += 1
        word = random.choice(difficulty_list)

        random_word_list.extend([word])

    #delete \n

    random_word_list = list(map(lambda st: str.replace(st, "\n", ''), random_word_list))

    random_words = random_word_list

    return random_words
