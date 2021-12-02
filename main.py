import time

import pygame.display
import pygame
import pygame_menu

import grille
import menu
import words_library

black = (255,255,255)

pygame.init()

screen = pygame.display.set_mode((700, 700))

fond_start = pygame.image.load("motscroises.jpeg").convert()
fond_start = pygame.transform.scale(fond_start, (700, 700))
screen.fill(black)

running=True
time = pygame.time.Clock()

while running:

    for event in pygame.event.get():

        #screen.blit(fond_start, (0, 0))
        pygame.display.flip()
        menu.start_menu(screen,fond_start)

        if event.type == pygame.QUIT:
            running= False

time.tick(30)
#if __name__ == "__main__":




