import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.SysFont('Arial', 18)

# Set up the clock
clock = pygame.time.Clock()

# Set up the timer
start_time = pygame.time.get_ticks()

# Game loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current time
    current_time = pygame.time.get_ticks()

    # Calculate the elapsed time
    elapsed_time = current_time - start_time

    # Render the elapsed time
    text = font.render('Time Elapsed: {} ms'.format(elapsed_time), True, BLACK)

    # Clear the screen
    screen.fill(WHITE)

    # Blit the text
    screen.blit(text, (0, 40))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)