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

x = 100
y = 100
x2 = 0
y2 = 0
moveX = 0
moveY = 0

snakeSpeed = 5

frog = pygame.image.load("assets/frog_2.png")
game_bg = pygame.image.load("assets/snake_bg.png")
collisionSound = pygame.mixer.Sound("assets/point.wav")
bg_music = pygame.mixer.Sound("assets/music_1.wav")
# bg_music.play(-1)
counter = 0
# font = pygame.font.SysFont("assets/font_1.ttf", 30)
font = pygame.font.SysFont(None, 30)

snakeBody = []
snakeLength = 1

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:  # key was pressed
            if event.key == pygame.K_DOWN:  # down arrow key was pressed
                moveY = snakeSpeed
            if event.key == pygame.K_UP:
                moveY = -snakeSpeed
            if event.key == pygame.K_LEFT:
                moveX = -snakeSpeed
            if event.key == pygame.K_RIGHT:
                moveX = snakeSpeed

    screen.fill(white)
    msg = f"Score : {counter}"
    # render(msg to show, sharpness, color)
    renderedMsg = font.render(msg, True, red)
    screen.blit(renderedMsg, (10, 10))
    # screen.blit(game_bg, (0, 0))

    color = random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)
    # surface, color, (x,y,width,height)
    pygame.draw.rect(screen, blue, (x, y, 50, 50))
    pygame.draw.rect(screen, green, (x2, y2, 50, 50))

    x += moveX
    y += moveY

    pygame.display.update()
