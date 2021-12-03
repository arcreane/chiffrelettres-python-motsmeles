import time

import pygame.display
import pygame
import pygame_menu

import grille
import menu
import timer
import words_library

# Game loop definition

def run():

    black = (0,0,0)

    pygame.init()

    screen = pygame.display.set_mode((900, 603))
    #wallpaper parameters
    fond_start = pygame.image.load("motscroises.jpeg").convert()
    fond_start = pygame.transform.scale(fond_start, (900, 603))
    screen.fill(black)

    running=True
    time = pygame.time.Clock()


    font = pygame.freetype.SysFont(None, 42)
    font.origin = True
    selection = False
    while running:
        screen.blit(fond_start, (0, 0))
        if not selection:
            menu.start_menu(screen, font)
        selection = True
        timer.timer(screen)

        grille.grille(screen, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running= False

        pygame.display.flip()

    time.tick(30)

if __name__ == "__main__":
    run()




