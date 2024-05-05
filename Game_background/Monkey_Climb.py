# ------------------------------------------------------ IMPORTING ------------------------------------------------------
import pygame
from pygame.locals import *
pygame.init()


# ------------------------------------------------------ SCREEN ------------------------------------------------------
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Platformer')


# ------------------------------------------------------ VARIABLES ------------------------------------------------------
TILE_SIZE = 50
MAIN_MENU = True
TITLE = 'MONEY CLIMB'
CLOCK = pygame.time.Clock()
FPS = 60


# ------------------------------------------------------ IMAGES ------------------------------------------------------
# ----- MENU -----
MENU_IMG = pygame.image.load('Images/Monkey_Climb.jpeg')
MIR = (1400, 900)
MENU_IMG = pygame.transform.scale(MENU_IMG, MIR)


# ----- BUTTONS -----
START_BUTTON_IMG = pygame.image.load('Images/Buttons/Start_Button.jpeg')
SBI_RESIZE = (200, 100)
START_BUTTON_IMG = pygame.transform.scale(START_BUTTON_IMG, SBI_RESIZE)

EXIT_BUTTON_IMG = pygame.image.load('Images/Buttons/Exit_Button.jpeg')
EBI_RESIZE = (200, 100)
EXIT_BUTTON_IMG = pygame.transform.scale(EXIT_BUTTON_IMG, EBI_RESIZE)


# ----- LEVEL -----
LVL_BG_IMG = pygame.image.load('Images/LEVEL_ASSETS/Level_IMG.jpg')
LVL_BG_IMG_resized = (1400,900)
LVL_BG_IMG = pygame.transform.scale(LVL_BG_IMG, LVL_BG_IMG_resized)

GROUND_IMG = pygame.image.load('Images/LEVEL_ASSETS/Ground_asset.jpg')

TRUNK_01_IMG = pygame.image.load('Images/LEVEL_ASSETS/Trunk_asset_01.jpg')

TRUNK_02_IMG = pygame.image.load('Images/LEVEL_ASSETS/Trunk_asset_02.jpg')

TRUNK_03_IMG = pygame.image.load('Images/LEVEL_ASSETS/Trunk_asset_03.jpg')

CENTER_BRANCH_IMG = pygame.image.load('Images/LEVEL_ASSETS/Center_branch_asset.jpg')


def draw_grid():
	for line in range(0, 29):
		pygame.draw.line(SCREEN, (255, 255, 255), (0, line * TILE_SIZE), (SCREEN_WIDTH, line * TILE_SIZE))
		pygame.draw.line(SCREEN, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, SCREEN_HEIGHT))



# ------------------------------------------------------ CLASS ------------------------------------------------------
class Player():
	def __init__ (self, x, y):
		img = pygame.image.load('Images/Monkey/back_monkey.jpg')
		self.image = pygame.transform.scale(img, (40, 80))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.vel_y = 0
		self.jumped = False

	def update(self):
		
		dx = 0
		dy = 0

		#get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE] and self.jumped == False:
			self.vel_y = -15
			self.jumped = True

		if key[pygame.K_SPACE] == False:
			self.jumped = False

		if key[pygame.K_LEFT]:
			dx -= 5

		if key[pygame.K_RIGHT]:
			dx += 5

		#add gravity 
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		dy += self.vel_y
		
		#check for collision
  
		#update player coordinates
		self.rect.x += dx
		self.rect.y += dy

		if self.rect.bottom > SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT
			dy = 0

		#draw player onto screen
		SCREEN.blit(self.image, self.rect)



class World():
	def __init__(self, data):
		self.tile_list = []

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(GROUND_IMG, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(TRUNK_01_IMG, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					img = pygame.transform.scale(TRUNK_02_IMG, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 4:
					img = pygame.transform.scale(TRUNK_03_IMG, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 5:
					img = pygame.transform.scale(CENTER_BRANCH_IMG, (TILE_SIZE, TILE_SIZE // 2))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			SCREEN.blit(tile[0], tile[1])

class Button():
	def __init__ (self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()
		
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
				
		#draw button
		SCREEN.blit(self.image, self.rect)
		return action



# ------------------------------------------------------ INSTANCES ------------------------------------------------------
#WORLD
world_data = [
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 4],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[2, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
world = World(world_data)

#MONKEY
player = Player(100, SCREEN_HEIGHT - 130)

#BUTTON
start_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150, START_BUTTON_IMG)
exit_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 300, EXIT_BUTTON_IMG)






run = True
while run:

	CLOCK.tick(FPS)
	
	if MAIN_MENU == True:
		SCREEN.blit(MENU_IMG, (0, 0))

		if exit_button.draw():
			run = False

		if start_button.draw():
			MAIN_MENU = False

	else:
		SCREEN.blit(LVL_BG_IMG, (0, 0))
		world.draw()
		player.update()
		draw_grid()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
