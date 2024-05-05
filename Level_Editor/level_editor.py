import pygame 
import button
import csv
pygame.init()

#game window
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
LOWER_MARGIN = 100
SIDE_MARGIN = 300

SCREEN = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')


#defining game variables
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ROWS = 18

font = pygame.font.SysFont('Futura', 30)

MAX_COLS = 28
TILE_SIZE = 50
TILE_TYPES = 6
level = 0
current_tile = 0

#load images
lvl_img = pygame.image.load('test/LEVEL_ASSETS/level_IMG.jpg')
r_lvl_img = (1400, 900)
lvl_img = pygame.transform.scale(lvl_img, r_lvl_img)
#store tiles in list
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'test/LEVEL_ASSETS/{x}.png').convert_alpha()
    
    if x == 0:
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    if x == 1:
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    if x == 2:
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    if x == 3:
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    if x == 4:
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE // 2))
    if x == 5:
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

save_img = pygame.image.load('test/LEVEL_ASSETS/save_btn.png').convert_alpha()
load_img = pygame.image.load('test/LEVEL_ASSETS/load_btn.png').convert_alpha()

#create empty tile list
world_data = []
for row in range (ROWS):
    r = [-1] * MAX_COLS
    world_data.append(r)

#create ground
for tile in range(0, MAX_COLS):
    world_data[ROWS - 1][tile] = 0

# function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    SCREEN.blit(img, (x, y))


#create function for drawing background
def draw_bg():
    SCREEN.fill(GREEN)
    SCREEN.blit(lvl_img, (0, 0))


#draw grid
def draw_grid():
    #veritcal lines
    for c in range(MAX_COLS + 1):
        pygame.draw.line(SCREEN, WHITE, (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGHT))
    #horizontal lines
    for c in range(ROWS + 1):
        pygame.draw.line(SCREEN, WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))


#function for drawing the world tiles
def draw_world():
    for y , row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                SCREEN.blit(img_list[tile], (x * TILE_SIZE, y * TILE_SIZE))

#create buttons
save_button = button.Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT + LOWER_MARGIN - 50, save_img, 1)
load_button = button.Button(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT + LOWER_MARGIN - 50, load_img, 1)

#make a button list
button_list = []
button_col = 0
button_row = 0
for i in range(len(img_list)):
    tile_button = button.Button(SCREEN_WIDTH + (75 * button_col) + 50, 75 * button_row + 50, img_list[i], 1)
    button_list.append(tile_button)
    button_col += 1
    if button_col == 3:
        button_row += 1
        button_col = 0



run = True
while run:

    draw_bg()
    draw_grid()
    draw_world()

    draw_text(f'Level: {level}', font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 90)
    draw_text('Press UP or DOWN to change level', font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 60)

    #save and load data
    if save_button.draw(SCREEN):
        #save level data
        with open(f'level{level}_data.csv', 'w', newline = '') as csvfile:
            writer =csv.writer(csvfile, delimiter = ',')
            for row in world_data:
                writer.writerow(row)

    if load_button.draw(SCREEN):
        #load in level data
        with open(f'level{level}_data.csv', newline = '') as csvfile:
            reader =csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    world_data[x][y] = int(tile)


    #draw tile panel and titles
    pygame.draw.rect(SCREEN, GREEN, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))
    
    #chose a tile
    button_count = 0
    for button_count, i in enumerate(button_list):
       if i.draw(SCREEN):
           current_tile = button_count
    
    #highlight the selected tile
    pygame.draw.rect(SCREEN, RED, button_list[current_tile].rect, 3)
        















    #add new tiles to the screen
    #get mouse pos
    pos = pygame.mouse.get_pos()
    x = (pos[0]) // TILE_SIZE
    y = (pos[1]) // TILE_SIZE

    # check that the coords are in the tile area
    if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
        #update tile value
        if pygame.mouse.get_pressed()[0] == 1:
            if world_data[y][x] != current_tile:
                world_data[y][x] = current_tile
        if pygame.mouse.get_pressed()[2] == 1:
            world_data[y][x] = -1
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and level <= 3:
            if event.key == pygame.K_UP:
                level += 1
            elif event.key == pygame.K_DOWN and level > 0:
                level -= 1
    
    pygame.display.update()
pygame.quit()