import random


def import_library():

    #Get liste_francais.txt and pass it througt a Python list named library

    extract = open("liste_francais.txt")
    library = extract.readlines()

    library = list(map(lambda st: str.replace(st, "?", "e"), library))

    random_words_library(library)

def random_words_library(list):

    word_list = []
    i = 0
    while i < 4:#difficulté select

        i += 1
        word = random.choice(list)
        word_list.extend([word])

    print(word_list)



#     cut_word(word_list)
#
# def cut_word (list):
#     i=0
#     letter_list = []
#     for letter in list:
#         i+=1
#         letter_list = list(list[i])
#
#
#     print(letter_list)



#if len(world list) > nombre cases