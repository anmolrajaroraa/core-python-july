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
    redPlayer = pygame.image.load("assets/red-player.png")
    yellowPlayer = pygame.image.load("assets/yellow-player.png")
    bluePlayer = pygame.image.load("assets/blue-player.png")
    greenPlayer = pygame.image.load("assets/green-player.png")
    greenCoord1 = 60
    greenCoord2 = 60
    redCoord1 = 350
    redCoord2 = 60
    blueCoord1 = 350
    blueCoord2 = 360
    yellowCoord1 = 60
    yellowCoord2 = 360
    greenDirection = "left"
    availableBoxesForGreen = [[43, 214], [76, 214], [109, 214], [142, 214], [175, 214], [208, 181], [208, 148], [208, 115], [208, 82], [208, 49], [208, 16], [241, 16], [274, 16], [274, 49], [274, 82], [274, 115], [274, 148], [274, 181], [307, 214], [340, 214], [373, 214], [406, 214], [439, 214], [472, 214], [472, 247], [
        472, 280], [439, 280], [406, 280], [373, 280], [340, 280], [307, 280], [274, 313], [274, 346], [274, 379], [274, 412], [274, 445], [274, 478], [241, 478], [208, 478], [208, 445], [208, 412], [208, 379], [208, 346], [208, 313], [175, 280], [142, 280], [109, 280], [76, 280], [43, 280], [10, 280], [10, 247], [43, 247], [76, 247], [109, 247], [142, 247], [175, 247]]
    availableBoxesForRed = [[274, 49], [274, 82], [274, 115], [274, 148], [274, 181], [307, 214], [340, 214], [373, 214], [406, 214], [439, 214], [472, 214], [472, 247], [
        472, 280], [439, 280], [406, 280], [373, 280], [340, 280], [307, 280], [274, 313], [274, 346], [274, 379], [274, 412], [274, 445], [274, 478], [241, 478], [208, 478], [208, 445], [208, 412], [208, 379], [208, 346], [208, 313], [175, 280], [142, 280], [109, 280], [76, 280], [43, 280], [10, 280], [10, 247], [10, 214], [43, 214], [76, 214], [109, 214], [142, 214], [175, 214], [208, 181], [208, 148], [208, 115], [208, 82], [208, 49], [208, 16], [241, 16], [241, 49], [241, 82], [241, 115], [241, 148], [241, 181]]
    availableBoxesForYellow = [[208, 445], [208, 412], [208, 379], [208, 346], [208, 313], [175, 280], [142, 280], [109, 280], [76, 280], [43, 280], [10, 280], [10, 247], [10, 214], [43, 214], [76, 214], [109, 214], [142, 214], [175, 214], [208, 181], [208, 148], [208, 115], [208, 82], [208, 49], [208, 16], [241, 16], [274, 16], [274, 49], [
        274, 82], [274, 115], [274, 148], [274, 181], [307, 214], [340, 214], [373, 214], [406, 214], [439, 214], [472, 214], [472, 247], [472, 280], [439, 280], [406, 280], [373, 280], [340, 280], [307, 280], [274, 313], [274, 346], [274, 379], [274, 412], [274, 445], [274, 478], [241, 478], [241, 445], [241, 412], [241, 379], [241, 346], [241, 313]]
    availableBoxesForBlue = [[439, 280], [406, 280], [373, 280], [340, 280], [307, 280], [274, 313], [274, 346], [274, 379], [274, 412], [274, 445], [274, 478], [241, 478], [208, 478], [208, 445], [208, 412], [208, 379], [208, 346], [208, 313], [175, 280], [142, 280], [109, 280], [76, 280], [43, 280], [10, 280], [10, 247], [10, 214], [43, 214], [
        76, 214], [109, 214], [142, 214], [175, 214], [208, 181], [208, 148], [208, 115], [208, 82], [208, 49], [208, 16], [241, 16], [274, 16], [274, 49], [274, 82], [274, 115], [274, 148], [274, 181], [307, 214], [340, 214], [373, 214], [406, 214], [439, 214], [472, 214], [472, 247], [439, 247], [406, 247], [373, 247], [340, 247], [307, 247]]
#[274, 49], [274, 82], [274, 115], [274, 148], [274, 181], [307, 214], [340, 214], [373, 214], [406, 214], [439, 214], [472, 214], [472, 247], [472, 280],

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    if len(availableBoxesForGreen) == 0:
                        greenCoord1 = 208
                        greenCoord2 = 247
                    if len(availableBoxesForGreen) > 0:
                        greenCoord1 = availableBoxesForGreen[0][0]
                        greenCoord2 = availableBoxesForGreen[0][1]
                        availableBoxesForGreen.pop(0)
                if event.key == pygame.K_r:
                    if len(availableBoxesForRed) == 0:
                        redCoord1 = 241
                        redCoord2 = 214
                    if len(availableBoxesForRed) > 0:
                        redCoord1 = availableBoxesForRed[0][0]
                        redCoord2 = availableBoxesForRed[0][1]
                        availableBoxesForRed.pop(0)
                if event.key == pygame.K_y:
                    if len(availableBoxesForYellow) == 0:
                        yellowCoord1 = 241
                        yellowCoord2 = 280
                    if len(availableBoxesForYellow) > 0:
                        yellowCoord1 = availableBoxesForYellow[0][0]
                        yellowCoord2 = availableBoxesForYellow[0][1]
                        availableBoxesForYellow.pop(0)
                if event.key == pygame.K_b:
                    if len(availableBoxesForBlue) == 0:
                        blueCoord1 = 274
                        blueCoord2 = 247
                    if len(availableBoxesForBlue) > 0:
                        blueCoord1 = availableBoxesForBlue[0][0]
                        blueCoord2 = availableBoxesForBlue[0][1]
                        availableBoxesForBlue.pop(0)
                    # if len(availableBoxes) > 2:
                    #     availableBoxes.remove([coord1, coord2])
                    #     temp_coord1 = coord1
                    #     temp_coord2 = coord2
                    #     if [temp_coord1 - 33, temp_coord2] in availableBoxes:
                    #         coord1 = temp_coord1 - 33
                    #         coord2 = temp_coord2
                    #         greenDirection = "left"
                    #     elif [temp_coord1, temp_coord2 - 33] in availableBoxes:
                    #         coord1 = temp_coord1
                    #         coord2 = temp_coord2 - 33
                    #         greenDirection = "up"
                    #     elif [temp_coord1 + 33, temp_coord2] in availableBoxes:
                    #         coord1 = temp_coord1 + 33
                    #         coord2 = temp_coord2
                    #         greenDirection = "right"
                    #     elif [temp_coord1 + 33, temp_coord2 - 33] in availableBoxes:
                    #         coord1 = temp_coord1 + 33
                    #         coord2 = temp_coord2 - 33
                    #         greenDirection = "up"
                    #     elif [temp_coord1, temp_coord2 + 33] in availableBoxes:
                    #         coord1 = temp_coord1
                    #         coord2 = temp_coord2 + 33
                    #         greenDirection = "down"
                    #     elif [temp_coord1 + 33, temp_coord2 + 33] in availableBoxes:
                    #         coord1 = temp_coord1 + 33
                    #         coord2 = temp_coord2 + 33
                    #         greenDirection = "right"
                    #     elif [temp_coord1 - 33, temp_coord2 + 33] in availableBoxes:
                    #         coord1 = temp_coord1 - 33
                    #         coord2 = temp_coord2 + 33
                    #         greenDirection = "down"
                    #     elif [temp_coord1 - 33, temp_coord2 - 33] in availableBoxes:
                    #         coord1 = temp_coord1 - 33
                    #         coord2 = temp_coord2 - 33
                    #         greenDirection = "left"

        # availableBoxes = []
        screen.fill(black)
        screen.blit(greenHouse, (10, 18))
        screen.blit(redHouse, (303, 18))
        screen.blit(blueHouse, (303, 312))
        screen.blit(yellowHouse, (10, 312))
        screen.blit(centerImage, (205, 216))

        for x in range(208, 285, 33):
            for y in range(313, 500, 33):
                # availableBoxes.append([x, y])
                pygame.draw.rect(screen, yellow, (x, y, 30, 30))

        for y in range(16, 200, 33):
            for x in range(208, 285, 33):
                # availableBoxes.append([x, y])
                pygame.draw.rect(screen, red, (x, y, 30, 30))

        for x in range(10, 180, 33):
            for y in range(214, 285, 33):
                # availableBoxes.append([x, y])
                pygame.draw.rect(screen, green, (x, y, 30, 30))

        for x in range(307, 475, 33):
            for y in range(214, 285, 33):
                # availableBoxes.append([x, y])
                pygame.draw.rect(screen, blue, (x, y, 30, 30))

        screen.blit(greenPlayer, (greenCoord1, greenCoord2))
        screen.blit(greenPlayer, (125, 60))
        screen.blit(greenPlayer, (125, 130))
        screen.blit(greenPlayer, (60, 130))

        screen.blit(bluePlayer, (blueCoord1, blueCoord2))
        screen.blit(bluePlayer, (415, 360))
        screen.blit(bluePlayer, (415, 430))
        screen.blit(bluePlayer, (350, 430))

        screen.blit(redPlayer, (redCoord1, redCoord2))
        screen.blit(redPlayer, (415, 60))
        screen.blit(redPlayer, (415, 130))
        screen.blit(redPlayer, (350, 130))

        screen.blit(yellowPlayer, (yellowCoord1, yellowCoord2))
        screen.blit(yellowPlayer, (125, 360))
        screen.blit(yellowPlayer, (125, 430))
        screen.blit(yellowPlayer, (60, 430))

        # print(availableBoxes)

        pygame.display.update()


splashScreen()
