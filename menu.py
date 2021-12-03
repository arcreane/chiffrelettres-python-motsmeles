import pygame
import pygame_menu

import grille


def set_difficulty(value, difficulty):
    # Do the job here !
    pass


def start_the_game():
    pass

def start_menu(screen, fond_start):


    menu = pygame_menu.Menu('Welcome to mots croises', 500, 500,theme=pygame_menu.themes.THEME_BLUE)
    menu.add.dropselect('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=set_difficulty)
    menu.add.button('Play', )
    menu.add.button('Quit', pygame_menu.events.EXIT)
    pygame.display.flip()

    menu.mainloop(screen)




