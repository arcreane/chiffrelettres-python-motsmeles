import time

import pygame.display
import pygame
import pygame_menu

import grille
import menu
import timer
import words_library
width=900
heigth= 603
def run():
    black = (0,0,0)

    pygame.init()

    screen = pygame.display.set_mode((width, heigth))

    fond_start = pygame.image.load("motscroises.jpeg").convert()
    fond_start = pygame.transform.scale(fond_start, (width, heigth))
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
        #words_library.import_library()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running= False

        pygame.display.flip()

    time.tick(30)

if __name__ == "__main__":
    run()




