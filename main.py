import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # background colour black
        screen.fill('black')
        # update sprites
        for sprite in updatable:
            sprite.update(dt)
        # detect collisions
        for asteroid in asteroids:
            if asteroid.is_colliding_with(player):
                print('Game over!')
                return
        # draw sprites
        for sprite in drawable:
            sprite.draw(screen)
        # refresh the screen
        pygame.display.flip()
        # pause for constant 60 fps
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()
