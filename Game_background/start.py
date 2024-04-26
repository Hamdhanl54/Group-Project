import pygame
import sys
from PIL import Image
import requests
from io import BytesIO


# ---------- Variables ----------
SCREENWIDTH = 750
SCREENHEIGHT = 900
FPS = 1


# ---------- Class ----------
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)

        self.states = {'start': self.start, 'level': self.level}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self.gameStateManager.set_state('level')

            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)


class Start:
    def __init__ (self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        


        # -- IMAGE --
        # Background
        self.back_image_url = 'https://raw.githubusercontent.com/Hamdhanl54/Group-Project/main/Images/Monkey_Climb.jpeg'
        back_response = requests.get(self.back_image_url)
        self.back_image_data = back_response.content
        back_pil_image = Image.open(BytesIO(self.back_image_data))
        back_resized_pil_image = back_pil_image.resize((800, 1000))
        back_resized_image_bytes = BytesIO()
        back_resized_pil_image.save(back_resized_image_bytes, format = 'PNG')
        back_resized_image_bytes.seek(0)
        self.back_start_image = pygame.image.load(back_resized_image_bytes)


    def run(self):
        self.display.blit(self.start_image, (0,0))
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