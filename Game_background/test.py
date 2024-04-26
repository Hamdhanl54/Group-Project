import pygame
screen_height = 500
screen_width = 600

screen = pygame.display.set_mode((screen_width, screen_height))

play_img = pygame.image.load('Images/PlayButton.png').convert_alpha()

quit_img = pygame.image.load('Images/QuitButton.png').convert_alpha()


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()
        
        #cehck mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

play_button = Button(50, 200, play_img, 0.2)
quit_button = Button(200, 200, quit_img, 0.2)

run = True
while run:

    screen.fill((202, 226, 241))

    if play_button.draw():
        print('Start')

    if quit_button.draw():
        print('Quit')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

