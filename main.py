import pygame

from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # background colour black
        screen.fill((0, 0, 0))
        # refresh the screen
        pygame.display.flip()
        # pause for constant 60 fps
        dt = clock.tick(60) / 1000


if __name__ == '__main__':
    main()
