class Player(pygame.sprite.Sprite):
2    def __init__(self):
3        super().__init__()
4        self.image = pygame.Surface((50, 50))
5        self.image.fill((255, 0, 0))
6        self.rect = self.image.get_rect()
7        self.frame = 0
8        self.health = 10
9        self.is_jumping = True
10        self.is_falling = False
11        self.movey = 0
12
13    def jump(self):
14        if self.is_jumping is False:
15            self.is_falling = False
16            self.is_jumping = True
17
18    def update(self):
19        if self.is_jumping and self.is_falling is False:
20            self.is_falling = True
21            self.movey -= 33  # how high to jump
22
23        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
24        for g in ground_hit_list:
25            self.movey = 0
26            self.rect.bottom = g.rect.top
27            self.is_jumping = False  # stop jumping
28
29        # fall off the world
30        if self.rect.y > worldy:
31            self.health -=1
32            print(self.health)
33            self.rect.x = tx
34            self.rect.y = ty
35
36        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
37        for p in plat_hit_list:
38            self.is_jumping = False  # stop jumping
39            self.movey = 0
40
41            # approach from below
42            if self.rect.bottom <= p.rect.bottom:
43               self.rect.bottom = p.rect.top
44            else:
45               self.movey += 3.2
46
47        if self.movey > 0:
48            self.is_jumping = True  # turn gravity on
49            self.frame += 1
50            if self.frame > 3 * ani:
51                self.frame = 0
52            self.image = self.images[self.frame // ani]
53
54        self.rect.y += self.movey