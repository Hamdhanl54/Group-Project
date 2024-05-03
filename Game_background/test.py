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


# ------------------------------------------------------ IMAGES ------------------------------------------------------
#MENU
#BUTTONS

#LEVEL
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

	def draw(self):
		SCREEN.blit(self.image, self.rect)


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

#BUTTON
restart_button = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 100, restart_img)

run = True
while run:

	SCREEN.blit(LVL_BG_IMG, (0, 0))

	world.draw()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()