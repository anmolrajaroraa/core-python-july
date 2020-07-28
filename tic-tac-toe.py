gamePositions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    print(f'''
    {gamePositions[0]} | {gamePositions[1]} | {gamePositions[2]}
    ---------
    {gamePositions[3]} | {gamePositions[4]} | {gamePositions[5]}
    ---------
    {gamePositions[6]} | {gamePositions[7]} | {gamePositions[8]}
    ''')
    userInput = int(input("User turn: "))
    userInput = userInput - 1
    gamePositions[userInput] = 'X'
# gamePositions[5] = 'O'
