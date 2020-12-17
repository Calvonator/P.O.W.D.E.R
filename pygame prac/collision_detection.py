import pygame, sys, random
from pygame.locals import *

#Setup Pygame
pygame.init()
main_clock = pygame.time.Clock()

#Setup window
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Collision Detection")

#Setup colours
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

#Setup player and food data structures
food_counter = 0
new_food = 40
food_size = 20

player = pygame.Rect(300, 100, 50, 50)

foods = []

for _ in range(20):
    foods.append(pygame.Rect(random.randint(0, SCREEN_WIDTH - food_size), random.randint(0, SCREEN_HEIGHT - food_size), food_size, food_size))

#Setup movement variables
move_left = False
move_right = False
move_up = False
move_down = False

move_speed = 6

#Game loop

running = True

while running:

    #Check for events
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            running = False
        
        if event.type == KEYDOWN:
        
            #Change keyboard variables

            if event.key == K_LEFT or event.key == K_a:
                move_right = False
                move_left = True

            if event.key == K_RIGHT or event.key == K_d:
                move_left = False
                move_right = True

            if event.key == K_UP or event.key == K_w:
                move_down = False
                move_up = True
            
            if event.key == K_DOWN or event.key == K_s:
                move_up = False
                move_down = True

        if event.type == KEYUP:

            if event.key == K_LEFT or event.key == K_a:
                move_left = False

            if event.key == K_RIGHT or event.key == K_d:
                move_right = False

            if event.key == K_UP or event.key == K_w:
                move_up = False
            
            if event.key == K_DOWN or event.key == K_s:
                move_down = False

            if event.key == K_x:
                player.top = random.randint(0, SCREEN_HEIGHT - player.height)
                player.left = random.randint(0, SCREEN_WIDTH - player.width)

        
        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.po[0], event.pos[1], food_size, food_size))

    food_counter += 1

    if food_counter >= new_food:
        #Add new food

        food_counter = 0
        foods.append(pygame.Rect(random.randint(0, SCREEN_WIDTH - food_size), random.randint(0, SCREEN_HEIGHT - food_size), food_size, food_size))


    #Draw white background onto screen
    screen.fill(WHITE)

    #Move the player
    if  move_down and player.bottom < SCREEN_HEIGHT:
        player.top += move_speed

    if move_up and player.top > 0:
        player.top -= move_speed

    if move_left and player.left > 0:
        player.left -= move_speed

    if move_right and player.right < SCREEN_WIDTH:
        player.right += move_speed

    #Draw player on surface 
    pygame.draw.rect(screen, BLACK, player)

    #Check whether the player has intersected with any food squares
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    #Draw the food
    for i in range(len(foods)):
        pygame.draw.rect(screen, GREEN, foods[i])

    #Draw window onto (actual) screen
    pygame.display.update()
    main_clock.tick(40)
