import pygame
import sys
import os
import pygame.freetype 

def render_score(screen, score, font_size=24, font_color=(255, 255, 255), x_offset = 300):
    font = pygame.freetype.SysFont('Arial', font_size)
    text_surface, _ = font.render(f'Score: {score}', font_color)
    text_rect = text_surface.get_rect(center=((screen.get_width() // 2), 30))
    screen.blit(text_surface, text_rect)

# Initialize Pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Set up some variables
player_score = 0
computer_score = 0
num_games = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
    # Clear the screen
    screen.fill((0, 0, 0))

    # Display the score
    render_score(screen, player_score)
    render_score(screen, computer_score, font_size=20, font_color=(255, 0, 0), x_offset=300)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()