import random

from termcolor import colored

gamePositions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
winningPositions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
    0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

print("\033[91m \033[1m \033[4m Tic Tac Toe \033[0m".center(22))
# print(colored("Tic Tac Toe".center(22), "red"))

while True:
    userChoice = input("What do you want to use (X/O): ")
    if userChoice == 'x' or userChoice == 'X':
        userChoice = "X"
        cpuChoice = "O"
        print("You selected X")
        break
    elif userChoice == "O" or userChoice == 'o' or userChoice == '0':
        userChoice = "O"
        cpuChoice = "X"
        print("You selected O")
        break
    else:
        print("Invalid choice...")

print(f'''
    {gamePositions[0]} | {gamePositions[1]} | {gamePositions[2]}
    ---------
    {gamePositions[3]} | {gamePositions[4]} | {gamePositions[5]}
    ---------
    {gamePositions[6]} | {gamePositions[7]} | {gamePositions[8]}
''')

isUserTurn = True
userTurnsPlayed = 0
isGameFinished = False

while not isGameFinished and userTurnsPlayed < 5:
    if isUserTurn:
        userInput = int(input("Enter the position: "))
        if userInput in gamePositions:
            gamePositions[userInput - 1] = userChoice
            userTurnsPlayed += 1
            isUserTurn = False
        else:
            print("Position already occupied...")
            continue
    else:
        cpuInput = random.choice(gamePositions)
        print("cpu input is", cpuInput)
        if cpuInput == "X" or cpuInput == "O":
            continue
        gamePositions[cpuInput - 1] = cpuChoice
        isUserTurn = True

    print(f'''
    {gamePositions[0]} | {gamePositions[1]} | {gamePositions[2]}
    ---------
    {gamePositions[3]} | {gamePositions[4]} | {gamePositions[5]}
    ---------
    {gamePositions[6]} | {gamePositions[7]} | {gamePositions[8]}
    ''')

    if userTurnsPlayed >= 3:
        for position in winningPositions:
            # print(position)   [0,1,2]   [3,4,5]
            if gamePositions[position[0]] == gamePositions[position[1]] and gamePositions[position[0]] == gamePositions[position[2]]:
                isGameFinished = True
                print("CPU wins") if isUserTurn else print("User wins")
                # if isUserTurn:
                #     print("CPU wins")
                # else:
                #     print("User wins")
                break

if not isGameFinished:
    print("Game draw")
