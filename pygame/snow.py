import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BEIGE = (244, 226, 198)

class snow:
    def __init__(self):
        self.y = random.randint(0,720)
        self.x = random.randint(10,1280)
        self.colour = WHITE
        self.width = random.randint(8,16)
        self.speed = random.randint(3,8)

    def draw(self):
        pygame.draw.rect(screen, self.colour,(self.x, self.y, self.width, self.width))

    def update(self):
        if self.y > 720:
            self.x = random.randint(0,1280)
            self.y = random.randint(0,20)
        else:
            self.y += self.speed

class house:
    def __init__(self):
        self.y = 400
        self.x = 400
        self.colour = BEIGE
        self.width = 150
        self.height = 100
    def draw(self):
        pygame.draw.rect(screen, self.colour,(self.x, self.y, self.width, self.width))

pygame.init()


# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")
 
# Loop until the user clicks the close button.
done = False
# Variables
house1 = house()
snowgroup = []
for i in range(100):
    snowgroup.append(snow())

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    house1.draw()
    for i in snowgroup:
        i.draw()
        i.update()
    
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
