import random

gameChoices = ["stone", "paper", "scissors"]

print('''
    1. Stone
    2. Paper
    3. Scissors
''')

userWins = 0
cpuWins = 0
gameDraw = 0

while userWins < 3 and cpuWins < 3:
    userInput = int(input("User turn: "))
    if userInput < 1 or userInput > 3:
        continue
    userInput = userInput - 1
    userInput = gameChoices[userInput]
    cpuInput = random.choice(gameChoices)
    print("User input: ", userInput)
    print("Cpu input: ", cpuInput)
    if userInput == cpuInput:
        print("Game draw")
        gameDraw += 1
    elif userInput == "stone":
        if cpuInput == "paper":
            print("CPU wins")
            cpuWins += 1
        else:
            print("User wins")
            userWins += 1
    elif userInput == "paper":
        if cpuInput == "stone":
            print("User wins")
            userWins += 1
        else:
            print("CPU wins")
            cpuWins += 1
    else:
        if cpuInput == "stone":
            print("CPU wins")
            cpuWins += 1
        else:
            print("User wins")
            userWins += 1

    print(
        f"Score -> User : {userWins}, CPU : {cpuWins}, Draw : {gameDraw}, Total Matches : {userWins + cpuWins + gameDraw}")
