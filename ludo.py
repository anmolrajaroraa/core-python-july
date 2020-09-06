import pygame
import random
pygame.init()

width = 512
height = 512

screen = pygame.display.set_mode((width, height))

# red, green, blue (rgb) 0-255
# 0-255, 0-255, 0-255
white = 255, 255, 255
black = 0, 0, 0
blue = 51, 150, 228
green = 67, 150, 71
red = 242, 29, 29
yellow = 243, 210, 72


def splashScreen():
    ludoBg = pygame.image.load("assets/ludobg.png")
    msg = "Press SPACE to start game"
    font = pygame.font.SysFont("assets/font_1.ttf", 50)
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    startGame()
        screen.blit(ludoBg, (0, 0))
        randomColor = random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)
        renderedMsg = font.render(msg, True, randomColor)
        screen.blit(renderedMsg, (28, 470))

        pygame.display.update()


def startGame():
    greenHouse = pygame.image.load("assets/green.png")
    redHouse = pygame.image.load("assets/red.png")
    yellowHouse = pygame.image.load("assets/yellow.png")
    blueHouse = pygame.image.load("assets/blue.png")
    centerImage = pygame.image.load("assets/center.png")
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)
        screen.blit(greenHouse, (10, 18))
        screen.blit(redHouse, (303, 18))
        screen.blit(blueHouse, (303, 312))
        screen.blit(yellowHouse, (10, 312))
        screen.blit(centerImage, (205, 216))

        for y in range(310, 500, 33):
            for x in range(205, 285, 33):
                pygame.draw.rect(screen, yellow, (x, y, 30, 30))

        for y in range(20, 200, 33):
            for x in range(205, 285, 33):
                pygame.draw.rect(screen, red, (x, y, 30, 30))

        for x in range(10, 180, 33):
            for y in range(214, 285, 33):
                pygame.draw.rect(screen, green, (x, y, 30, 30))

        for x in range(300, 475, 33):
            for y in range(214, 285, 33):
                pygame.draw.rect(screen, blue, (x, y, 30, 30))

        pygame.display.update()


splashScreen()
