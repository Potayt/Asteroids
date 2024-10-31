# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    fpsclock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable,)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    #Make game objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    newfield = AsteroidField()

    #Run loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = fpsclock.tick(60) / 1000
        for x in updatable:
            x.update(dt)
        screen.fill("black")
        for y in drawable:
            y.draw(screen)
        for z in asteroids:
            if (z.collide(player1)):
                print("Game over!")
                sys.exit()
            for t in shots:
                if (z.collide(t)):
                    z.split()
                    t.kill()

        pygame.display.flip()
        



if __name__ == "__main__":
    main()