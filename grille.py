import pygame
import words_library

width=900
heigth= 600
game_grid_width=width//3*2
surface=game_grid_width*heigth
nb_col = 15

col_width = game_grid_width / nb_col
lin_height = heigth / nb_col

gris=(60,60,60)
black=(0,0,0)
white=(255,255,255)

easy = 7
horizontal = 0
vertical = 1
diagonal = 2
#position 0, le mot
#position 1 direction
#position 2 ordre (normal ou reverse)
#position 3 coord

mots = [("coding", horizontal,False, (5,4)), ("factory", vertical, True, (12,3)), ("arcreane", diagonal, True, (0,6))]

def grille(screen, font):
    grid = []
    col = []
    lin = []
    pygame.display.set_caption("Mot Mélee")

    carre=(0,0,game_grid_width,heigth)#create game grid
    pygame.draw.rect(screen, gris,carre)#display game grid

    for i in range( nb_col+1):#create a line for grid
            grid.append(pygame.rect.Rect(i * col_width, 0, 3, heigth))
            grid.append(pygame.rect.Rect(0, i * lin_height, game_grid_width, 3))
            if i != nb_col:#coordonée
                col.append(i * col_width)
                lin.append(i * lin_height)

# for i in range(nb_col):
#        print("col", col[i])
#       print("line", lin[i])
    for trace in range(nb_col+1):#display line
        pygame.draw.rect(screen, white, grid[2 * trace])
        pygame.draw.rect(screen, white, grid[2 * trace + 1])



    #for i in range(len(col)):
    #    for j in range (1,len(lin)+1):
    #        font.render_to(screen, (i*col_width +6, j*lin_height-3), "A", pygame.Color('red'))

    for word in mots:#def of horizon,vartical,diagonal and reverse
        coords = word[3]
        letter_postion = 0
        inc_h = 0
        inc_vert = 0
        if word[1] == horizontal:
            inc_h = 1
        elif word[1] == vertical:
            inc_vert = 1
        elif word[1] == diagonal:
            inc_h = 1
            inc_vert = 1

            #reverse
        order = 1
        if word[2] == True:
            order = -1
        for letter in word[0][::order]:

            #placement to the word in the grid
            font.render_to(screen, ((coords[0] + letter_postion*inc_h)* col_width + 6,
                                    (coords[1] +1 + letter_postion*inc_vert)* lin_height- 3), letter, pygame.Color('red'))
            letter_postion +=1

