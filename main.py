import time

import pygame.display
import pygame
import pygame_menu

import grille
import menu
import timer
import words_library

black = (255,255,255)

pygame.init()

screen = pygame.display.set_mode((900, 603))

fond_start = pygame.image.load("motscroises.jpeg").convert()
fond_start = pygame.transform.scale(fond_start, (700, 700))
screen.fill(black)

running=True
time = pygame.time.Clock()

font = pygame.freetype.SysFont(None, 42)
font.origin = True

while running:
    screen.blit(fond_start, (0, 0))
    grille.grille(screen, font)
    #menu.start_menu(screen, fond_start)
    timer.timer(screen)
    #words_library.import_library()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    pygame.display.flip()

time.tick(30)
#if __name__ == "__main__":




