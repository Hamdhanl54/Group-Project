# ------------------------------------------------------ IMPORTING ------------------------------------------------------
import pygame
from pygame.locals import *
import pickle
from os import path
pygame.init()


# ------------------------------------------------------ SCREEN ------------------------------------------------------
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Monkey Climb')


# ------------------------------------------------------ VARIABLES ------------------------------------------------------
TILE_SIZE = 50
game_over = 0
MAIN_MENU = True
OBJ_MENU = True
PAUSE_MENU = False
menu_state = "Main"
level = 1
max_levels = 10
TITLE = 'MONEY CLIMB'
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont('font.ttf', 20)
FPS = 60


# ------------------------------------------------------ IMAGES ------------------------------------------------------
# ----- MENU -----
MENU_IMG = pygame.image.load('Images/Monkey_Climb.jpeg')
MIR = (1400, 900)
MENU_IMG = pygame.transform.scale(MENU_IMG, MIR)

OBJ_IMG = pygame.image.load('Images/Objective.jpg')
OIR = (1400, 900)
OBJ_IMG = pygame.transform.scale(OBJ_IMG, OIR)


# ----- BUTTONS -----
START_BUTTON_IMG = pygame.image.load('Images/Buttons/Start_Button.jpeg')
SBI_RESIZE = (200, 100)
START_BUTTON_IMG = pygame.transform.scale(START_BUTTON_IMG, SBI_RESIZE)

EXIT_BUTTON_IMG = pygame.image.load('Images/Buttons/Exit_Button.jpeg')
EBI_RESIZE = (200, 100)
EXIT_BUTTON_IMG = pygame.transform.scale(EXIT_BUTTON_IMG, EBI_RESIZE)

OBJ_BUTTON_IMG = pygame.image.load('Images/Buttons/Objective_Button.jpeg')
OBI_RESIZE = (200, 100)
OBJ_BUTTON_IMG = pygame.transform.scale(OBJ_BUTTON_IMG, OBI_RESIZE)

BACK_BUTTON_IMG = pygame.image.load('Images/Buttons/BACK_BUTTON.png')
BBI_RESIZE = (200, 100)
BACK_BUTTON_IMG = pygame.transform.scale(BACK_BUTTON_IMG, BBI_RESIZE)

RESUME_BUTTON_IMG = pygame.image.load('Images/Buttons/Resume_Button.png')
RBI_RESIZE = (200, 100)
RESUME_BUTTON_IMG = pygame.transform.scale(RESUME_BUTTON_IMG, RBI_RESIZE)

PAUSE_EXIT_BUTTON_IMG = pygame.image.load('Images/Buttons/Pause_Exit_Button.png')
PEBI_RESIZE = (200, 100)
PAUSE_EXIT_BUTTON_IMG = pygame.transform.scale(PAUSE_EXIT_BUTTON_IMG, PEBI_RESIZE)


# ----- LEVEL -----
LVL_BG_IMG = pygame.image.load('Images/LEVEL_ASSETS/Level_IMG.jpg')
LVL_BG_IMG_resized = (1400,900)
LVL_BG_IMG = pygame.transform.scale(LVL_BG_IMG, LVL_BG_IMG_resized)

GROUND_IMG = pygame.image.load('Images/LEVEL_ASSETS/Ground_asset.jpg')

TRUNK_01_IMG = pygame.image.load('Images/LEVEL_ASSETS/Trunk_asset_01.jpg')

TRUNK_02_IMG = pygame.image.load('Images/LEVEL_ASSETS/Trunk_asset_02.jpg')

TRUNK_03_IMG = pygame.image.load('Images/LEVEL_ASSETS/Trunk_asset_03.jpg')

CENTER_BRANCH_IMG = pygame.image.load('Images/LEVEL_ASSETS/Center_branch_asset.jpg')

LADDER_IMG = pygame.image.load('Images/LEVEL_ASSETS/Ladder_asset.png')

FAKE_CENTER = pygame.image.load('Images/LEVEL_ASSETS/Center_branch_asset.jpg')

FAKE_LADDER = pygame.image.load('Images/LEVEL_ASSETS/Ladder_asset.png')


# ------------------------------------------------------ FUNCTIONS ------------------------------------------------------
def reset_level(level):
	player.reset(100, SCREEN_HEIGHT - 130)
	exit_group.empty()
	fake_exit_grounp.empty()
	if path.exists(f'level{level}_data'):
		pickle_in = open(f'level{level}_data', 'rb')
	world_data = pickle.load(pickle_in)
	world = World(world_data)

	return world


# ------------------------------------------------------ CLASS ------------------------------------------------------
class World():
	def __init__(self, data):
		self.tile_list = []
		self.fake_center_platfroms = []
		self.fake_ladder = []

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 0:
					img = pygame.transform.scale(GROUND_IMG, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 1:
					img = pygame.transform.scale(TRUNK_02_IMG, (TILE_SIZE, TILE_SIZE))
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
					img = pygame.transform.scale(TRUNK_03_IMG, (TILE_SIZE, TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 4:
					img = pygame.transform.scale(CENTER_BRANCH_IMG, (TILE_SIZE, TILE_SIZE // 2))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 5:
					exit = Exit(col_count * TILE_SIZE, row_count * TILE_SIZE - (TILE_SIZE * 2))
					exit_group.add(exit)
				if tile == 6:
					img = pygame.transform.scale(FAKE_CENTER, (TILE_SIZE, TILE_SIZE // 2))
					img_rect = img.get_rect()
					img_rect.x = col_count * TILE_SIZE
					img_rect.y = row_count * TILE_SIZE
					self.fake_center_platfroms.append((img, img_rect))
				if tile == 7:
					fake_exit = Exit(col_count * TILE_SIZE, row_count * TILE_SIZE - (TILE_SIZE * 2))
					fake_exit_grounp.add(fake_exit)

				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			SCREEN.blit(tile[0], tile[1])
		for platform in self.fake_center_platfroms:
			SCREEN.blit(platform[0], platform[1])
		for ladder in self.fake_ladder:
			SCREEN.blit(ladder[0], ladder[1])
			#pygame.draw.rect(SCREEN, (255, 255, 255), tile[1], 2)

class Player():
	def __init__ (self, x, y):
		self.reset(x, y)
		

	def update(self, game_over):
		
		dx = 0
		dy = 0
		idle_cooldown = 3
		right_cooldown = 3
		jump_cooldown = 0

		if game_over == 0:

			#get keypresses
			key = pygame.key.get_pressed()
			
				
			if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
				self.vel_y = -20
				self.jumped = True
				#jump animation
				self.counter += 1
				if self.counter > jump_cooldown:
					self.counter = 0
					self.index += 1
					if self.index >=len(self.images_jump):
						self.index = 0
						

		
			if key[pygame.K_SPACE] == False:
				self.jumped = False
				

			if key[pygame.K_LEFT]:
				dx -= 9
				self.counter += 1
				self.direction = -1
				#right and left
				self.counter += 1
				if self.counter > right_cooldown:
					self.counter = 0
					self.index += 1
					if self.index >= len(self.images_right):
						self.index = 0
					if self.direction == 1:
						self.image = self.images_right[self.index]
					if self.direction == -1:
						self.image = self.images_left[self.index]

			if key[pygame.K_RIGHT]:
				dx += 9
				self.counter += 1
				self.direction = 1
				#right and left
				self.counter += 1
				if self.counter > right_cooldown:
					self.counter = 0
					self.index += 1
					if self.index >= len(self.images_right):
						self.index = 0
					if self.direction == 1:
						self.image = self.images_right[self.index]
					if self.direction == -1:
						self.image = self.images_left[self.index]
			
			if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
				#handle animation
				#idle
				self.idle_counter += 1
				if self.idle_counter > idle_cooldown:
					self.idle_counter = 0
					self.idle_index += 1
					if self.idle_index >= len(self.images_idle):
						self.idle_index = 0
					self.image = self.images_idle[self.idle_index]

			#add gravity 
			self.vel_y += 1
			if self.vel_y > 10:
				self.vel_y = 10
			dy += self.vel_y
			
			#check for collision
			self.in_air = True
			for tile in world.tile_list:
				#chech for collision in the x direction
				if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
					dx = 0
				#check for collisions in the y direction
				if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
					#check if below the ground i.e. jumping
					if self.vel_y < 0:
						dy = tile[1].bottom - self.rect.top
						self.vel_y = 0
					#check if above the ground i.e. falling
					elif self.vel_y >= 0:
						dy = tile[1].top - self.rect.bottom
						self.vel_y = 0
						self.in_air = False
			
			#check collision with exit
			if pygame.sprite.spritecollide(self, exit_group, False):
				game_over = 1
	
			#update player coordinates
			self.rect.x += dx
			self.rect.y += dy

		#draw player onto screen
		SCREEN.blit(self.image, self.rect)

		return game_over
	
	def reset(self, x, y):
		#idleing animations
		self.images_idle = []
		self.idle_index = 0
		self.idle_counter = 0
		for num in range (0, 158):
			img_idle = pygame.image.load(f'Images/Monkey/Idleing/{num}.png')
			img_idle = pygame.transform.scale(img_idle, (TILE_SIZE, 60))
			self.images_idle.append(img_idle)
		self.image = self.images_idle[self.idle_index]
		
        #left and right animations
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		for num in range (0, 12):
			img_left = pygame.image.load(f'Images/Monkey/Right&Left/{num}.png')
			img_left = pygame.transform.scale(img_left, (TILE_SIZE, 60))
			img_right = pygame.transform.flip(img_left, True, False)
			self.images_left.append(img_left)
			self.images_right.append(img_right)
		self.image = self.images_right[self.index]

		#Jumping animation
		self.images_jump = []
		self.jump_index = 0
		self.jump_counter = 0
		for num in range (0, 7):
			img_jump = pygame.image.load(f'Images/Monkey/Jumping/{num}.png')
			img_jump = pygame.transform.scale(img_jump, (TILE_SIZE, 60))
			self.images_jump.append(img_jump)
		self.image = self.images_jump[self.index]
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0
		self.in_air = True

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

class Exit(pygame.sprite.Sprite):
	def __init__ (self, x, y):
		pygame.sprite.Sprite.__init__ (self)
		img = LADDER_IMG
		self.image = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE * 3))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

# ------------------------------------------------------ INSTANCES ------------------------------------------------------

#Groups
exit_group = pygame.sprite.Group()
fake_exit_grounp = pygame.sprite.Group()


#MONKEY
player = Player(100, SCREEN_HEIGHT - 130)

#WORLD
#load in level data
if path.exists(f'level{level}_data'):
	pickle_in = open(f'level{level}_data', 'rb')
	world_data = pickle.load(pickle_in)
world = World(world_data)

#BUTTON
start_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, START_BUTTON_IMG)
exit_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 300, EXIT_BUTTON_IMG)
obj_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150, OBJ_BUTTON_IMG)
back_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 150, BACK_BUTTON_IMG)
resume_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 150, RESUME_BUTTON_IMG)
pause_exit_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, PAUSE_EXIT_BUTTON_IMG)


run = True
while run:

	CLOCK.tick(FPS)
	
	if menu_state == "Objective":
		SCREEN.blit(OBJ_IMG, (0,0))
		MAIN_MENU = False
		
		if back_button.draw():
			menu_state = 'Main'
			MAIN_MENU = True

	if menu_state == 'Main':
		if MAIN_MENU:
			SCREEN.blit(MENU_IMG, (0, 0))

			if exit_button.draw():
				run = False

			if start_button.draw():
				MAIN_MENU = False
			
			if obj_button.draw():
				menu_state = "Objective"
		

		else:
			if PAUSE_MENU == True:
				if resume_button.draw():
					PAUSE_MENU = False
				elif pause_exit_button.draw():
					run = False
			else:
				SCREEN.blit(LVL_BG_IMG, (0, 0))
				world.draw()
				player.update(game_over)
				exit_group.draw(SCREEN)
				fake_exit_grounp.draw(SCREEN)
				fake_exit_grounp.draw(SCREEN)
				game_over = player.update(game_over)


				#if player has completed level
				if game_over == 1:
					#reset game and go to next level
					level += 1
					if level <= max_levels:
						#reset level
						world_data = []
						world = reset_level(level)
						game_over = 0
						pygame.display.set_caption(f'level #{level}')
					else:
						#restart game
						pass

			if player.rect.bottom > SCREEN_HEIGHT:
				level -= 1
				if path.exists(f'level{level}_data'):
					pickle_in = open(f'level{level}_data', 'rb')
					world_data = pickle.load(pickle_in)
					exit_group.empty()
					fake_exit_grounp.empty()
				world = World(world_data)
				player.rect.y = player.rect.y - (SCREEN_HEIGHT + player.rect.height)
		
		
			
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				PAUSE_MENU = True
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
