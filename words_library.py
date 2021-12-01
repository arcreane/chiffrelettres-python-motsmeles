import random


def import_library():

    #Get the liste_francais.txt and pass it througt a Python list named library

    extract = open("liste_francais.txt")
    library = extract.readlines()

    library = list(map(lambda st: str.replace(st, "?", "e"), library))

    print(library)

    random_words_library(library)

def random_words_library(list):

    i=0
    while i < 4:#difficulté select
        i+=1
        print(random.choice(list))


