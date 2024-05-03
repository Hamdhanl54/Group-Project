# ------------------------------------------------------ IMPORTING ------------------------------------------------------
import pygame
import sys
from pygame.locals import *
pygame.init()


# ------------------------------------------------------ SCREEN ------------------------------------------------------
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 900
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monkey CLimb Menu")


# ------------------------------------------------------ IMAGES ------------------------------------------------------
BACKGROUND_IMG = pygame.image.load('Images/Monkey_Climb.jpeg')
BACKGROUND_SCALE = (750, 900)
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, BACKGROUND_SCALE)

PLAY_BUTTON_IMG = pygame.image.load("Images/Start_Button.jpeg")
PLAY_BUTTON_SCALE = (200, 100)
PLAY_BUTTON_IMG = pygame.transform.scale(PLAY_BUTTON_IMG, PLAY_BUTTON_SCALE)

OBJ_BUTTON_IMG = pygame.image.load("Images/Objective_Button.jpeg")
OBJ_BUTTON_SCALE = (200, 100)
OBJ_BUTTON_IMG = pygame.transform.scale(OBJ_BUTTON_IMG, OBJ_BUTTON_SCALE)

EXIT_BUTTON_IMG = pygame.image.load("Images/Exit_Button.jpeg")
EXIT_BUTTON_SCALE = (200, 100)
EXIT_BUTTON_IMG = pygame.transform.scale(EXIT_BUTTON_IMG, EXIT_BUTTON_SCALE)

BACK_BUTTON_IMG = pygame.image.load("Images/BACK_BUTTON.png")
BACK_BUTTON_SCALE = (200, 100)
BACK_BUTTON_IMG = pygame.transform.scale(BACK_BUTTON_IMG, BACK_BUTTON_SCALE)

OBJ_IMG = pygame.image.load("Images/Objective.jpg")
OBJ_IMG_SCALE = (750, 900)
OBJ_IMG = pygame.transform.scale(OBJ_IMG, OBJ_IMG_SCALE)


# ------------------------------------------------------ CLASS ------------------------------------------------------
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)


# ------------------------------------------------------ DEFINING ------------------------------------------------------
def get_font(size):
    return pygame.font.Font("font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def objective():
    while True:
        OBJECTIVE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(OBJ_IMG, (0, 0))

        OBJECTIVE_BACK = Button(image=BACK_BUTTON_IMG, pos=(375, 840), 
                            text_input="", font=get_font(75), base_color="Black", hovering_color="Green")

        OBJECTIVE_BACK.changeColor(OBJECTIVE_MOUSE_POS)
        OBJECTIVE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OBJECTIVE_BACK.checkForInput(OBJECTIVE_MOUSE_POS):
                    main_menu()

        pygame.display.update()


# ------------------------------------------------------ MAIN MENU ------------------------------------------------------
def main_menu():
    while True:
        SCREEN.blit(BACKGROUND_IMG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MONKEY CLIMB", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(375, 100))

        PLAY_BUTTON = Button(image=PLAY_BUTTON_IMG, pos=(120, 840), 
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        OBJECTIVE_BUTTON = Button(image=OBJ_BUTTON_IMG, pos=(375, 840), 
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=EXIT_BUTTON_IMG, pos=(630, 840), 
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OBJECTIVE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OBJECTIVE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    objective()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()