import pygame
import time
import random

pygame.init()

pygame.display.set_caption("Snake! By William Mathias")

grid_width = 20
grid_height = 20
grid_margin = 1

grid_dimx = 12
grid_dimy = 9

display_width = grid_dimx * (grid_width + grid_margin) + grid_margin
display_height = grid_dimy * (grid_height + grid_margin) + grid_margin

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

color1 = black
color2 = green

game_display = pygame.display.set_mode((display_width, display_height))

for row in range(0, grid_dimy): #this loop reates the display grid
    for column in range(0, grid_dimx):
        pygame.draw.rect(game_display, color1, [column * (grid_width + grid_margin) + grid_margin, row * (grid_height + grid_margin) + grid_margin, grid_width, grid_height])


clock = pygame.time.Clock()

def draw_snake(snake_list):
    for i in snake_list:
        pygame.draw.rect(game_display, color2, [i[0] * (grid_width + grid_margin) + grid_margin, i[1] * (grid_height + grid_margin) + grid_margin, grid_width, grid_height])

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 25)
    TextSurf, TextRect = text_objects(text, large_text)
    TextRect.center = ((display_width/2), (display_height/2))
    game_display.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    game_display.fill(color1)
    message_display('Game Over')

def game_loop():

    apple_matrix = []
    for x in range(grid_dimx):
        for y in range(grid_dimy):
            apple_matrix.append([x, y])

    snake_len = 1
    snake_lst = []

    snakex = round(grid_dimx/2) - 1
    snakey = round(grid_dimy/2) - 1

    apple = random.choice(apple_matrix)
    applex = apple[0]
    appley = apple[1]

    snake_changex = 0
    snake_changey = 0
    
    game_exit = False
    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if snake_len == 1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        snake_changex = 1
                        snake_changey = 0
                    elif event.key == pygame.K_LEFT:
                        snake_changex = -1
                        snake_changey = 0
                    elif event.key == pygame.K_UP:
                        snake_changex = 0
                        snake_changey = -1
                    elif event.key == pygame.K_DOWN:
                        snake_changex = 0
                        snake_changey = 1
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if snake_changex != -1:
                            snake_changex = 1
                            snake_changey = 0
                    elif event.key == pygame.K_LEFT:
                        if snake_changex != 1:
                            snake_changex = -1
                            snake_changey = 0
                    elif event.key == pygame.K_UP:
                        if snake_changey != 1:
                            snake_changex = 0
                            snake_changey = -1
                    elif event.key == pygame.K_DOWN:
                        if snake_changey != -1:
                            snake_changex = 0
                            snake_changey = 1


        snakex += snake_changex
        snakey += snake_changey
        
        game_display.fill(color1)
        pygame.draw.rect(game_display, color2, [snakex * (grid_width + grid_margin) + grid_margin, snakey * (grid_height + grid_margin) + grid_margin, grid_width, grid_height])
        pygame.draw.rect(game_display, red, [applex * (grid_width + grid_margin) + grid_margin, appley * (grid_height + grid_margin) + grid_margin, grid_width, grid_height])

        if snakex > grid_dimx - 1 or snakex < 0 or snakey < 0 or snakey > grid_dimy - 1:
            crash()

        snake_head = []
        snake_head.append(snakex)
        snake_head.append(snakey)
        snake_lst.append(snake_head)
        if len(snake_lst) > snake_len:
            snake_lst.pop(0)

        for i in snake_lst[:-1]:
            if i == snake_head:
                crash()

        draw_snake(snake_lst)

        pygame.display.update()

        if snakex == applex and snakey == appley:
            apple_matrix = []
            for x in range(grid_dimx):
                for y in range(grid_dimy):
                    apple_matrix.append([x, y])
            for block in snake_lst:
                apple_matrix = [i for i in apple_matrix if i != block]
            apple = random.choice(apple_matrix)
            applex = apple[0]
            appley = apple[1]
            snake_len += 1

        clock.tick(8)

game_loop()
pygame.quit()
quit()