import pygame
import tkinter

# Initialing Color
color = (255, 0, 0)
# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((600, 600))
drawing = False
last_pos = None

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running=False

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                mouse_position = pygame.mouse.get_pos()
                if last_pos is not None:
                    pygame.draw.line(surface, color, last_pos, mouse_position, 10)
                last_pos = mouse_position
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_position = (0, 0)
            drawing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

        pygame.display.flip()


