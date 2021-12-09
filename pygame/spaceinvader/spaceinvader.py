import random
import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Alien(pygame.sprite.Sprite): 
# Define the constructor for Alien 
    def __init__(self, color, width, speed):
        self.speed = speed 
  # Call the sprite constructor 
        super().__init__() 
    # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,width]) 
        self.image.fill(color) 
    # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = random.randrange(0, 1280) 
        self.rect.y = random.randrange(0, 60) 
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > 720:
            self.rect.x = random.randrange(0, 1280) 
            self.rect.y = random.randrange(0, 60) 
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, speed, lives, bullet_count, score):
        self.bullet_count = bullet_count
        self.lives = lives
        self.speed = speed
        self.score = score
        super().__init__()

        self.image = pygame.Surface([width,width])
        self.image.fill(color)

        self.rect = self.image.get_rect() 

        self.rect.x = 0
        self.rect.y = 650
    def update(self):
        self.rect.x = self.rect.x + self.speed
        if self.rect.x > 1280:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = 1280
    def player_set_speed(self, s):
        self.speed = s

  #End Procedure
#End Class
class Bullet(pygame.sprite.Sprite):

    def __init__(self, color, x, y, speed):
        self.speed = speed 
  # Call the sprite constructor 
        super().__init__() 
    # Create a sprite and fill it with colour 
        self.image = pygame.Surface([5,5]) 
        self.image.fill(color) 
    # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.y = self.rect.y - self.speed



pygame.init()
size = (1280,720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space invader")
done = False
player = Player(GREEN, 50, 0, 5, 50, 0)
invader_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

number_of_aliens = 60

for x in range (number_of_aliens):
    width = random.randint(10,15)
    speed = 1
    my_Alien = Alien(RED,width,speed)
    invader_group.add(my_Alien)
    all_sprites_group.add(my_Alien)

all_sprites_group.add(player)

clock = pygame.time.Clock()

while not done:
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    bullet_hit_group = pygame.sprite.groupcollide(bullet_group, invader_group, True, True)
    for i in bullet_hit_group:
        score = player.score + 5
    for foo in player_hit_group:
        player.lives = player.lives - 1
    # --- Main event loop
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # - a key is down
            if event.key == pygame.K_LEFT: # - if the left key pressed
                player.player_set_speed(-3) # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                player.player_set_speed(3) # speed set to 3
            
            elif event.type == pygame.KEYUP: # - a key released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.player_set_speed(0) # speed set to 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player.bullet_count>0:
                bullet = Bullet(RED, int(player.rect.x+25), int(player.rect.y-25), 10)
                all_sprites_group.add(bullet)
                bullet_group.add(bullet)
            
    if player.lives == 0:
        done = True


    all_sprites_group.update()    
    screen.fill(BLACK)
    all_sprites_group.draw(screen)

    pygame.display.flip()  
    clock.tick(60)
pygame.quit()
print(player.score)