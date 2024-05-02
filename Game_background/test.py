import pygame
import sys

pygame.display.set_mode((50,50))

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()