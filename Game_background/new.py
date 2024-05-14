import pygame
import os

SW = 1400
SH = 900
SCREEN = pygame.display.set_mode((SW, SH))
pygame.display.set_caption('Monkey Climb')


# ----------------------------------------------------------------- VARIABLES -----------------------------------------------------------------
#player movement variables
moving_left = False
moving_right = False

#framerate variables
CLOCK = pygame.time.Clock()
FPS = 50

#game variables
GRAVITY = 0.75

#define colors
BG = (144, 201, 120)
RED = (255, 0, 0)

# ----------------------------------------------------------------- FUNCTIONS -----------------------------------------------------------------
def draw_bg():
    SCREEN.fill(BG)
    pygame.draw.line(SCREEN, RED, (0, 400), (SW, 400))


# ----------------------------------------------------------------- PLAYER -----------------------------------------------------------------
class Monkey(pygame.sprite.Sprite):
    def __init__ (self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 # 0 means idle, 1 means run
        self.update_time = pygame.time.get_ticks()
        
        #load all images for the monkey
        animation_type = ['Idleing', 'Right&Left', 'Jumping']
        
        for animation in animation_type:
            #reset temp list of images
            temp_list = []
            #count number of files in folder
            num_of_frames = len(os.listdir(f'Images/Monkey/{animation}'))
            for i in range (num_of_frames):
                img = pygame.image.load(f'Images/Monkey/{animation}/{i}.png')
                img = pygame.transform.scale(img, (50, 60))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def move(self, moving_left, moving_right):
        #reset movement variabls
        dx = 0
        dy = 0
        #assign movement variables if moving left or right
        #left
        if moving_left:
            dx = -self.speed
            self.flip = False
            self.direction = -1
        #right
        if moving_right:
            dx = self.speed
            self.flip = True
            self.direction = 1
        #jumping
        if self.jump == True and self.in_air == False:
            self.vel_y = -20
            self.jump = False
            self.in_air = True
        #apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        #check collision with floor
        if self.rect.bottom + dy > 400:
            dy = 400 - self.rect.bottom
            self.in_air = False

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy


    def update_animation(self):
        #update animation
        ANIMATION_COOLDOWN = 100
        #update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0


    def update_action(self, new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    def draw(self):
        SCREEN.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

monkey = Monkey(300, 300, 9)



run = True
while run:

    CLOCK.tick(FPS)
    draw_bg()

    #calling monkey
    monkey.update_animation()
    monkey.draw()

    #update monkey actions
    if monkey.in_air:
        monkey.update_action(2) #2: jump
    elif moving_left or moving_right:
        monkey.update_action(1) #1: run
    else:
        monkey.update_action(0) #0: idle
    monkey.move(moving_left, moving_right)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                monkey.jump = True
            if event.key == pygame.K_ESCAPE:
                run = False

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False



    pygame.display.update()
pygame.quit()