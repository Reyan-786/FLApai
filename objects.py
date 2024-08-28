import pygame
import random

# Constants
WIDTH, HEIGHT = 400, 600
BIRD_WIDTH, BIRD_HEIGHT = 34, 24
PIPE_WIDTH, PIPE_HEIGHT = 52, 320
GAP_SIZE = 150
GRAVITY = 1
FLAP_STRENGTH = -12 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Bird:  
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.image = pygame.image.load('bird1.png')  # Load the bird image
        self.image = pygame.transform.scale(self.image, (BIRD_WIDTH, BIRD_HEIGHT))  # Resize the image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        
    def flap(self):
        self.velocity = FLAP_STRENGTH
        
    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.topleft = (self.x, self.y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)  # Draw the bird image on the screen



class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.choice([50,60,70,80,90]) # random.randint(50, HEIGHT - GAP_SIZE - 50)
        self.rect_top = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.rect_bottom = pygame.Rect(self.x, self.height + GAP_SIZE, PIPE_WIDTH, HEIGHT - self.height - GAP_SIZE)

    def update(self):
        self.x -= 5
        self.rect_top.x = self.x
        self.rect_bottom.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect_top)
        pygame.draw.rect(screen, WHITE, self.rect_bottom)
