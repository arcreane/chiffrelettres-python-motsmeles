import pygame
import pygame.freetype

def timer(screen):

    clock=pygame.time.Clock()
    font=pygame.freetype.SysFont(None, 34)
    font.origin=True

    ticks = pygame.time.get_ticks()
    millis = ticks % 1000
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)
    out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
    font.render_to(screen, (650, 100), out, pygame.Color('red'))
    #clock.tick(60)

if __name__ == '__main__':
    timer()