import random


def import_library():

    #Get liste_francais.txt and pass it througt a Python list named library

    extract = open("liste_francais.txt")
    library = extract.readlines()

    library = list(map(lambda st: str.replace(st, "?", "e"), library))

    random_words_library(library)

def random_words_library(extracted_list):

    word_list = []
    i = 0
    while i < 4:#difficulté select

        i += 1
        word = random.choice(extracted_list)
        word_list.extend(word)

    #Cut words in letters

    word_list = list(map(lambda st: str.replace(st, "\n", ','), word_list))

    print(word_list)



#if len(world list) > nombre cases