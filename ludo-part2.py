import pygame
import random
from copy import deepcopy
from time import sleep
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
    redPlayer = pygame.image.load("assets/red-player.png")
    yellowPlayer = pygame.image.load("assets/yellow-player.png")
    bluePlayer = pygame.image.load("assets/blue-player.png")
    greenPlayer = pygame.image.load("assets/green-player.png")
    originalBoxesForGreen = [[43, 214], [76, 214], [109, 214], [142, 214], [175, 214], [208, 181], [208, 148], [208, 115], [208, 82], [208, 49], [208, 16], [241, 16], [274, 16], [274, 49], [274, 82], [274, 115], [274, 148], [274, 181], [307, 214], [340, 214], [373, 214], [406, 214], [439, 214], [472, 214], [472, 247], [
        472, 280], [439, 280], [406, 280], [373, 280], [340, 280], [307, 280], [274, 313], [274, 346], [274, 379], [274, 412], [274, 445], [274, 478], [241, 478], [208, 478], [208, 445], [208, 412], [208, 379], [208, 346], [208, 313], [175, 280], [142, 280], [109, 280], [76, 280], [43, 280], [10, 280], [10, 247], [43, 247], [76, 247], [109, 247], [142, 247], [175, 247]]
    originalBoxesForRed = [[274, 49], [274, 82], [274, 115], [274, 148], [274, 181], [307, 214], [340, 214], [373, 214], [406, 214], [439, 214], [472, 214], [472, 247], [
        472, 280], [439, 280], [406, 280], [373, 280], [340, 280], [307, 280], [274, 313], [274, 346], [274, 379], [274, 412], [274, 445], [274, 478], [241, 478], [208, 478], [208, 445], [208, 412], [208, 379], [208, 346], [208, 313], [175, 280], [142, 280], [109, 280], [76, 280], [43, 280], [10, 280], [10, 247], [10, 214], [43, 214], [76, 214], [109, 214], [142, 214], [175, 214], [208, 181], [208, 148], [208, 115], [208, 82], [208, 49], [208, 16], [241, 16], [241, 49], [241, 82], [241, 115], [241, 148], [241, 181]]
    originalBoxesForYellow = [[208, 445], [208, 412], [208, 379], [208, 346], [208, 313], [175, 280], [142, 280], [109, 280], [76, 280], [43, 280], [10, 280], [10, 247], [10, 214], [43, 214], [76, 214], [109, 214], [142, 214], [175, 214], [208, 181], [208, 148], [208, 115], [208, 82], [208, 49], [208, 16], [241, 16], [274, 16], [274, 49], [
        274, 82], [274, 115], [274, 148], [274, 181], [307, 214], [340, 214], [373, 214], [406, 214], [439, 214], [472, 214], [472, 247], [472, 280], [439, 280], [406, 280], [373, 280], [340, 280], [307, 280], [274, 313], [274, 346], [274, 379], [274, 412], [274, 445], [274, 478], [241, 478], [241, 445], [241, 412], [241, 379], [241, 346], [241, 313]]
    originalBoxesForBlue = [[439, 280], [406, 280], [373, 280], [340, 280], [307, 280], [274, 313], [274, 346], [274, 379], [274, 412], [274, 445], [274, 478], [241, 478], [208, 478], [208, 445], [208, 412], [208, 379], [208, 346], [208, 313], [175, 280], [142, 280], [109, 280], [76, 280], [43, 280], [10, 280], [10, 247], [10, 214], [43, 214], [
        76, 214], [109, 214], [142, 214], [175, 214], [208, 181], [208, 148], [208, 115], [208, 82], [208, 49], [208, 16], [241, 16], [274, 16], [274, 49], [274, 82], [274, 115], [274, 148], [274, 181], [307, 214], [340, 214], [373, 214], [406, 214], [439, 214], [472, 214], [472, 247], [439, 247], [406, 247], [373, 247], [340, 247], [307, 247]]

    turns = ["green", "red", "blue", "yellow"]
    currentTurn = "load"
    greenPlayersCoordinates = [[60, 60], [125, 60], [125, 130], [60, 130]]
    greenPlayersBoxes = [deepcopy(originalBoxesForGreen), deepcopy(
        originalBoxesForGreen), deepcopy(originalBoxesForGreen), deepcopy(originalBoxesForGreen)]
    greenPlayersOpened = [0, 0, 0, 0]
    redPlayersCoordinates = [[350, 60], [415, 60], [415, 130], [350, 130]]
    redPlayersBoxes = [deepcopy(originalBoxesForRed), deepcopy(
        originalBoxesForRed), deepcopy(originalBoxesForRed), deepcopy(originalBoxesForRed)]
    redPlayersOpened = [0, 0, 0, 0]
    bluePlayersCoordinates = [[350, 360], [415, 360], [415, 430], [350, 430]]
    bluePlayersBoxes = [deepcopy(originalBoxesForBlue), deepcopy(
        originalBoxesForBlue), deepcopy(originalBoxesForBlue), deepcopy(originalBoxesForBlue)]
    bluePlayersOpened = [0, 0, 0, 0]
    yellowPlayersCoordinates = [[60, 360], [125, 360], [125, 430], [60, 430]]
    yellowPlayersBoxes = [deepcopy(originalBoxesForYellow), deepcopy(
        originalBoxesForYellow), deepcopy(originalBoxesForYellow), deepcopy(originalBoxesForYellow)]
    yellowPlayersOpened = [0, 0, 0, 0]
    # 0 - not opened
    # 1 - opened
    # 2 - has reached destination

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

        for x in range(208, 285, 33):
            for y in range(313, 500, 33):
                pygame.draw.rect(screen, yellow, (x, y, 30, 30))

        for y in range(16, 200, 33):
            for x in range(208, 285, 33):
                pygame.draw.rect(screen, red, (x, y, 30, 30))

        for x in range(10, 180, 33):
            for y in range(214, 285, 33):
                pygame.draw.rect(screen, green, (x, y, 30, 30))

        for x in range(307, 475, 33):
            for y in range(214, 285, 33):
                pygame.draw.rect(screen, blue, (x, y, 30, 30))

        diceRoll = random.randint(1, 6)
        print("Dice rolled - ", diceRoll)

        if currentTurn == "load":
            currentTurn = "green"
        elif currentTurn == "green":
            playerNumber = int(input(
                f"Enter the number of {currentTurn} player which you want to move"))

            if (greenPlayersOpened[playerNumber - 1] == 0 and diceRoll == 1) or (greenPlayersOpened[playerNumber - 1] == 0 and diceRoll == 6):
                diceRoll = 1
                greenPlayersOpened[playerNumber - 1] = 1

            if (greenPlayersOpened[playerNumber - 1] == 1 and diceRoll <= (len(greenPlayersBoxes[playerNumber - 1]) + 1)):
                for i in range(diceRoll):
                    if len(greenPlayersBoxes[playerNumber - 1]) == 0:
                        greenPlayersCoordinates[playerNumber - 1][0] = 208
                        greenPlayersCoordinates[playerNumber - 1][1] = 247
                        greenPlayersOpened[playerNumber - 1] = 2
                    elif len(greenPlayersBoxes[playerNumber - 1]) > 0:
                        greenPlayersCoordinates[playerNumber -
                                                1][0] = greenPlayersBoxes[playerNumber - 1][0][0]
                        greenPlayersCoordinates[playerNumber -
                                                1][1] = greenPlayersBoxes[playerNumber - 1][0][1]
                        greenPlayersBoxes[playerNumber - 1].pop(0)
            currentTurn = "red"
        elif currentTurn == "red":
            playerNumber = int(input(
                f"Enter the number of {currentTurn} player which you want to move"))

            if (redPlayersOpened[playerNumber - 1] == 0 and diceRoll == 1) or (redPlayersOpened[playerNumber - 1] == 0 and diceRoll == 6):
                diceRoll = 1
                redPlayersOpened[playerNumber - 1] = 1

            if (redPlayersOpened[playerNumber - 1] == 1 and diceRoll <= (len(redPlayersBoxes[playerNumber - 1]) + 1)):
                for i in range(diceRoll):
                    if len(redPlayersBoxes[playerNumber - 1]) == 0:
                        redPlayersCoordinates[playerNumber - 1][0] = 241
                        redPlayersCoordinates[playerNumber - 1][1] = 214
                        redPlayersOpened[playerNumber - 1] = 2
                    elif len(redPlayersBoxes[playerNumber - 1]) > 0:
                        redPlayersCoordinates[playerNumber -
                                              1][0] = redPlayersBoxes[playerNumber - 1][0][0]
                        redPlayersCoordinates[playerNumber -
                                              1][1] = redPlayersBoxes[playerNumber - 1][0][1]
                        redPlayersBoxes[playerNumber - 1].pop(0)
            currentTurn = "blue"
        elif currentTurn == "blue":
            playerNumber = int(input(
                f"Enter the number of {currentTurn} player which you want to move"))

            if (bluePlayersOpened[playerNumber - 1] == 0 and diceRoll == 1) or (bluePlayersOpened[playerNumber - 1] == 0 and diceRoll == 6):
                diceRoll = 1
                bluePlayersOpened[playerNumber - 1] = 1

            if (bluePlayersOpened[playerNumber - 1] == 1 and diceRoll <= (len(bluePlayersBoxes[playerNumber - 1]) + 1)):
                for i in range(diceRoll):
                    if len(bluePlayersBoxes[playerNumber - 1]) == 0:
                        bluePlayersCoordinates[playerNumber - 1][0] = 274
                        bluePlayersCoordinates[playerNumber - 1][1] = 247
                        bluePlayersOpened[playerNumber - 1] = 2
                    elif len(bluePlayersBoxes[playerNumber - 1]) > 0:
                        bluePlayersCoordinates[playerNumber -
                                               1][0] = bluePlayersBoxes[playerNumber - 1][0][0]
                        bluePlayersCoordinates[playerNumber -
                                               1][1] = bluePlayersBoxes[playerNumber - 1][0][1]
                        bluePlayersBoxes[playerNumber - 1].pop(0)
            currentTurn = "yellow"
        elif currentTurn == "yellow":
            playerNumber = int(input(
                f"Enter the number of {currentTurn} player which you want to move"))

            if (yellowPlayersOpened[playerNumber - 1] == 0 and diceRoll == 1) or (yellowPlayersOpened[playerNumber - 1] == 0 and diceRoll == 6):
                diceRoll = 1
                yellowPlayersOpened[playerNumber - 1] = 1

            if (yellowPlayersOpened[playerNumber - 1] == 1 and diceRoll <= (len(yellowPlayersBoxes[playerNumber - 1]) + 1)):
                for i in range(diceRoll):
                    if len(yellowPlayersBoxes[playerNumber - 1]) == 0:
                        yellowPlayersCoordinates[playerNumber - 1][0] = 241
                        yellowPlayersCoordinates[playerNumber - 1][1] = 280
                        yellowPlayersOpened[playerNumber - 1] = 2
                    elif len(yellowPlayersBoxes[playerNumber - 1]) > 0:
                        yellowPlayersCoordinates[playerNumber -
                                                 1][0] = yellowPlayersBoxes[playerNumber - 1][0][0]
                        yellowPlayersCoordinates[playerNumber -
                                                 1][1] = yellowPlayersBoxes[playerNumber - 1][0][1]
                        yellowPlayersBoxes[playerNumber - 1].pop(0)
            currentTurn = "green"

        screen.blit(
            greenPlayer, (greenPlayersCoordinates[0][0], greenPlayersCoordinates[0][1]))
        screen.blit(
            greenPlayer, (greenPlayersCoordinates[1][0], greenPlayersCoordinates[1][1]))
        screen.blit(
            greenPlayer, (greenPlayersCoordinates[2][0], greenPlayersCoordinates[2][1]))
        screen.blit(
            greenPlayer, (greenPlayersCoordinates[3][0], greenPlayersCoordinates[3][1]))

        screen.blit(
            bluePlayer, (bluePlayersCoordinates[0][0], bluePlayersCoordinates[0][1]))
        screen.blit(
            bluePlayer, (bluePlayersCoordinates[1][0], bluePlayersCoordinates[1][1]))
        screen.blit(
            bluePlayer, (bluePlayersCoordinates[2][0], bluePlayersCoordinates[2][1]))
        screen.blit(
            bluePlayer, (bluePlayersCoordinates[3][0], greenPlayersCoordinates[3][1]))

        screen.blit(
            redPlayer, (redPlayersCoordinates[0][0], redPlayersCoordinates[0][1]))
        screen.blit(
            redPlayer, (redPlayersCoordinates[1][0], redPlayersCoordinates[1][1]))
        screen.blit(
            redPlayer, (redPlayersCoordinates[2][0], redPlayersCoordinates[2][1]))
        screen.blit(
            redPlayer, (redPlayersCoordinates[3][0], redPlayersCoordinates[3][1]))

        screen.blit(
            yellowPlayer, (yellowPlayersCoordinates[0][0], yellowPlayersCoordinates[0][1]))
        screen.blit(
            yellowPlayer, (yellowPlayersCoordinates[1][0], yellowPlayersCoordinates[1][1]))
        screen.blit(
            yellowPlayer, (yellowPlayersCoordinates[2][0], yellowPlayersCoordinates[2][1]))
        screen.blit(
            yellowPlayer, (yellowPlayersCoordinates[3][0], yellowPlayersCoordinates[3][1]))

        pygame.display.update()


splashScreen()
