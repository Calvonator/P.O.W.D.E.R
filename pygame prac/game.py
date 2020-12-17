import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)



pygame.init()



SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800


screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))


running = True

while running:

    for event in pygame.event.get():

        if event.type ==  KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))

    surf = pygame.Surface((50, 50))

    surf.fill((0, 0, 0))

    rect = surf.get_rect()

    screen.blit(surf, (SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2))

    pygame.display.flip()

