import random
import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Snow(pygame.sprite.Sprite): 
# Define the constructor for snow 
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
        self.rect.y = random.randrange(0, 400) 
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > 1280:
            self.rect.x = random.randrange(0, 1280) 
            self.rect.y = random.randrange(0, 400) 


  #End Procedure
#End Class
pygame.init()
size = (1280,720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
snow_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
number_of_flakes = 200

for x in range (number_of_flakes):
    width = random.randint(5,15)
    speed = random.randint(1,4)
    my_snow = Snow(WHITE,width,speed)
    snow_group.add(my_snow)
    all_sprites_group.add(my_snow)

clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    all_sprites_group.update()    
    screen.fill(BLACK)
    all_sprites_group.draw(screen)

    pygame.display.flip()  
    clock.tick(60)
pygame.quit()