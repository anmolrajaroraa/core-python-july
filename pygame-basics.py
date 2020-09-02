# pip install pygame
import pygame
import random
pygame.init()

width = 900
height = 500

screen = pygame.display.set_mode((width, height))

# red, green, blue (rgb) 0-255
# 0-255, 0-255, 0-255
white = 255, 255, 255
black = 0, 0, 0
blue = 50, 50, 255
green = 50, 255, 57
red = 242, 29, 29
color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
x = 100
y = 100
moveX = 1
moveY = 1

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x += moveX
    y += moveY
    screen.fill(green)

    # surface, color, (x,y), radius
    pygame.draw.circle(screen, color, (x, y), 50)

    pygame.display.update()
