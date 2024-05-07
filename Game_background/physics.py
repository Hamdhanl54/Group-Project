import pygame
import sys

monkey_velocity = 0
monkey_gravity = 0.5
monkey_jump_force = -10

# -------------------- POSITIONING -----------------------------------------

def update_monkey_position(monkey, delta_time):
    monkey.velocity += monkey_gravity * delta_time
    monkey.y += monkey.velocity * delta_time

#---------------------- Key Function for Jump -----------------------------
    def jump(monkey):
    monkey.velocity = monkey_jump_force


# ---------------------- Movement Functions -------------------------------

    def move_left(self):
        self.movex = -5

    def move_right(self):
        self.movex = 5
        
    def stop_moving_left(self):
        if self.movex < 0:
            self.movex = 0

    def stop_moving_right(self):
        if self.movex > 0:
            self.movex = 0

    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True

    def apply_gravity(self):
        if self.is_jumping and self.is_falling is False:
            self.is_falling = True
            self.movey -= self.jump_force
        elif self.is_falling:
            self.movey += self.gravity


# --------------------- Collision & Detection -----------------------------
    def update(self):
        self.rect.x += self.movex
        self.rect.y += self.movey

        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        for g in ground_hit_list:
            self.movey = 0
            self.rect.bottom = g.rect.top
            self.is_jumping = False  # stop jumping

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        for p in plat_hit_list:
            self.is_jumping = False  # stop jumping
            self.movey = 0

            # approach from below
            if self.rect.bottom <= p.rect.bottom:
               self.rect.bottom = p.rect.top
            else:
               self.movey += 3.2

        # apply gravity
        self.apply_gravity()

        # check for collision with walls
        if self.rect.x > worldx:
            self.rect.x = worldx
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > worldy:
            self.rect.y = worldy
        if self.rect.y < 0:
            self.rect.y = 0

# --------------------- GAME LOOP -----------------------------------------

while True:
    for event in pygame.event.get():
        if event.type ==pygame.Quit():
            pygame.quit()
            sys.exit()
    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jump(monkey)

    # Update monkey position
    update_monkey_position(monkey, delta_time)

    # Draw the game
    screen.fill((0, 0, 0))
    screen.blit(monkey_image, (monkey.x, monkey.y))
    pygame.display.flip()

# ------------------ Main Game Loop -------------------------------------------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                monkey.move_left()
            if event.key == pygame.K_RIGHT:
                monkey.move_right()
            if event.key == pygame.K_UP:
                monkey.jump()
            if event.key == pygame.K_DOWN:
                monkey.move_down()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                monkey.stop_moving_left()
            if event.key == pygame.K_
