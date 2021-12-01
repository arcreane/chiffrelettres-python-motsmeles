def import_library():

    extract = open("liste_francais.txt")
    raw_library = extract.readlines()
    library=[]

    for item in raw_library:
        number = 0
        while number < len(raw_library):
            library.append(str(item)+str(number))
            number += 1
    print(library)



def random_words_library():
    pass
