import pygame

from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # background colour black
        screen.fill('black')
        # draw the player
        player.draw(screen)
        # refresh the screen
        pygame.display.flip()
        # pause for constant 60 fps
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()
