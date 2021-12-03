import pygame
import pygame_menu

import grille
import main


def set_difficulty(value, difficulty):
    # Do the job here !
    pass


def start_the_game(screen, font, selection_menu):
    selection_menu.disable()



def start_menu(screen, font):

    menu_sel = pygame_menu.Menu('Welcome to mots croises', 500, 500,theme=pygame_menu.themes.THEME_BLUE)
    menu_sel.add.dropselect('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=set_difficulty)
    menu_sel.add.button('Play',start_the_game, screen, font, menu_sel)
    menu_sel.add.button('Quit', pygame_menu.events.EXIT)
    pygame.display.flip()
    menu_sel.mainloop(screen)





