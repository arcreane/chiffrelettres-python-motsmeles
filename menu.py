import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((800, 700))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Welcome to the Word Jumble', 600, 500,
                       theme=pygame_menu.themes.THEME_DARK)

# menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=set_difficulty)
menu.add.button('Play', start_the_game) #àfaire!
menu.add.button('Quit', pygame_menu.events.EXIT) #fonctionne!

menu.mainloop(surface)
