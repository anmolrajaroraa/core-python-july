import random

print("TIC_TAC_TOE".center(120))
player_1Choice = input("Choose your symbol- [X / 0]: ")
player_2Choice = "X" if player_1Choice == "0" else "0"
 
print(f"Player 1 : {player_1Choice}   Player 2 : {player_2Choice}")

gameProgress = [1,2,3,4,5,6,7,8,9]
availablePositions = [1,2,3,4,5,6,7,8,9]
# winningPositions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
winningPositions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
player_1Wins = 0
player_2Wins = 0
gameDraw = 0
player_1Turn = True
turnsPlayed = 0
gameOver = False
msg = "GAME DRAW"


gameBoard=f'''
       {gameProgress[0]}  |  {gameProgress[1]}  |  {gameProgress[2]}
       -------------
       {gameProgress[3]}  |  {gameProgress[4]}  |  {gameProgress[5]}
       -------------
       {gameProgress[6]}  |  {gameProgress[7]}  |  {gameProgress[8]}
       '''
print(gameBoard)
while not gameOver and len(availablePositions) > 0 :
    if player_1Turn:
        player_1Input = int(input("Player 1 \nEnter the position : "))
        if player_1Input not in availablePositions:
            print("Invalid Choice")
            continue
        availablePositions.remove(player_1Input)
        gameProgress[player_1Input - 1] = player_1Choice
        turnsPlayed += 1
        # player_1Turn = False
        # print(gameBoard) #list index out of range 
        # sirf ek if me rkhne se turnplayed vali condition nhi chl rhi 
        # ye gameProgress[position[0]] vagarh vali line nhi aayi smjh me 
        if turnsPlayed >= 3:
            # print("Entry 1")
            for position in winningPositions:
                # print("Entry 2")
                if gameProgress[position[0]] == gameProgress[position[1]] and gameProgress[position[1]] == gameProgress[position[2]]:
                    # print("Entry 3")
                    gameOver = True
                    if player_1Turn:
                        msg="Player 1 Won"
                    else:
                        msg="Player 2 Won" 
                    break
        
    else:

        player_2Input = int(input("Player 2 \nEnter the position : "))
        if player_2Input not in availablePositions:
            print("Invalid Choice")
            continue
        availablePositions.remove(player_2Input)
        gameProgress[player_2Input - 1] = player_2Choice
        # player_1Turn = True
        if turnsPlayed >= 3:
            # print("Entry 1")
            for position in winningPositions:
                # print("Entry 2")
                if gameProgress[position[0]] == gameProgress[position[1]] and gameProgress[position[1]] == gameProgress[position[2]]:
                    # print("Entry 3")
                    gameOver = True
                    if player_1Turn:
                        msg="Player 1 Won"
                    else:
                        msg="Player 2 Won" 
                    break

        
    
    
    player_1Turn = not player_1Turn
    gameBoard=f'''
    {gameProgress[0]}  |  {gameProgress[1]}  |  {gameProgress[2]}
    ------------
    {gameProgress[3]}  |  {gameProgress[4]}  |  {gameProgress[5]}
    ------------
    {gameProgress[6]}  |  {gameProgress[7]}  |  {gameProgress[8]}
    '''


    print(gameBoard)

print(msg)
    

