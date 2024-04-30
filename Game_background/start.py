import pygame
import sys


# ---------- Variables ----------
global SCREEN
global SCREENWIDTH
global SCREENHEIGHT
global FPS
SCREENWIDTH = 750
SCREENHEIGHT = 900
FPS = 1

# ----- Images -----
start_img = pygame.image.load('/Users/laiq/Desktop/Computer Science/Studio Code/03_Github/ICS4u/Images/Start_Button.jpeg')
start_size = (150,80)
start_img =  pygame.transform.scale(start_img, start_size)

exit_img = pygame.image.load('/Users/laiq/Desktop/Computer Science/Studio Code/03_Github/ICS4u/Images/Exit_Button.jpeg')
exit_size = (150,80)
exit_img = pygame.transform.scale(exit_img, exit_size)


# Background
back_img = pygame.image.load('/Users/laiq/Desktop/Computer Science/Studio Code/03_Github/ICS4u/Images/Monkey_Climb.jpeg')
back_size = (750, 900)
back_img = pygame.transform.scale(back_img, back_size)

#Monkey
monkey_img = pygame.image.load('/Users/laiq/Desktop/Computer Science/Studio Code/03_Github/ICS4u/Images/Back_Monkey.jpeg')
monkey_size = (240, 240)
monkey_img = pygame.transform.scale(monkey_img, monkey_size)

# ---------- Winndow ----------
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Monkey Climb')


# ---------- Initializing ----------


# ---------- Class ----------
class Game:
    def __init__(self):
        pygame.init()
      
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('start')
        self.start = Start(SCREEN, self.gameStateManager)
        self.level = Level(SCREEN, self.gameStateManager)

        self.states = {'start': self.start, 'level': self.level}

    def run(self):
        while True:

            SCREEN.blit(back_img, (0,0))
            SCREEN.blit(monkey_img, (285, 650))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self.gameStateManager.set_state('start')
                
                if event.type == pygame.KEYDOWN:
                    self.gameStateManager.set_state('level')


            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            pygame.display.flip() 
            self.clock.tick(FPS)
            

class Start:
    def __init__ (self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.gameStateManager.set_state('level')


class Level:
    def __init__ (self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    
    def run(self):
        self.display.fill('red')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.gameStateManager.set_state('start')

class GameStateManager:
    def __init__ (self, currentState):
        self.currentState = currentState
    
    def get_state(self):
        return self.currentState
    
    def set_state(self, state):
        self.currentState = state

if __name__ == '__main__':
    game = Game()
    game.run()