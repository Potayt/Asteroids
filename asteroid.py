import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"brown",self.position,self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        if (self.radius <= ASTEROID_MIN_RADIUS):
            self.kill()
            return
        randangle = random.uniform(20, 50)
        newang1 = self.velocity.rotate(randangle)
        newang2 = self.velocity.rotate(-randangle)
        newradius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position
        leftAst = Asteroid(x, y, newradius)
        leftAst.velocity = newang1 * 1.2
        rightAst = Asteroid(x, y, newradius)
        rightAst.velocity = newang2 * 1.2
        self.kill()
