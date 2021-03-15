# making visualization
xo = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

# GUI : Visualizing the TicTacToe Game (GameBoard)
def visualize(xo):
    print("-------------")
    for item in xo:
        print("| {} | {} | {} |".format(item[0], item[1], item[2]))
        print("-------------")
# TESTING
#visualize(xo)

# Input Function (Returning INDEX in The Board)
def inputIDXPlayer(isPlayer1):
    while True:
        try:
            if isPlayer1:
                res = int(input("Player 1, Enter the idx: "))
            else:
                res = int(input("Player 2, Enter the idx: "))
        except:
            print("Invalid input")
        else:
            break
    return res
#print(inputIDXPlayer(False))

# checking if any player are gonna win or not
def checkWin(xo):
    if xo[0] == ["O", "O", "O"] or xo[1] == ["O", "O", "O"] or xo[2] == ["O", "O", "O"]:
        return 1
    elif xo[0][0] == "O" and xo[1][1] == "O" and xo[2][2] == "O":
        return 1
    elif xo[0][2] == "O" and xo[1][1] == "O" and xo[2][0] == "O":
        return 1
    elif xo[0][0] == "O" and xo[1][0] == "O" and xo[2][0] == "O":
        return 1
    elif xo[0][1] == "O" and xo[1][1] == "O" and xo[2][1] == "O":
        return 1
    elif xo[0][2] == "O" and xo[1][2] == "O" and xo[2][2] == "O":
        return 1
    elif xo[0] == ["X", "X", "X"] or xo[1] == ["X", "X", "X"] or xo[2] == ["X", "X", "X"]:
        return 2
    elif xo[0][0] == "X" and xo[1][1] == "X" and xo[2][2] == "X":
        return 2
    elif xo[0][2] == "X" and xo[1][1] == "X" and xo[2][0] == "X":
        return 2
    elif xo[0][0] == "X" and xo[1][0] == "X" and xo[2][0] == "X":
        return 2
    elif xo[0][1] == "X" and xo[1][1] == "X" and xo[2][1] == "X":
        return 2
    elif xo[0][2] == "X" and xo[1][2] == "X" and xo[2][2] == "X":
        return 2

# The Logic of the game
def playingTicTacToe():
    # declaring state of player playing
    isPlayer1 = True
    while True:
        opt = input("Start(1 or any number except 2) Quit(2)")
        if opt == "2":
            print("QUITING THE GAME")
            break
        else:
            xo = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
            count = 0
            inputed = []
            while True:
                visualize(xo)
                print(inputed)
                if checkWin(xo) == 1:
                    print("PLAYER 1 WON")
                    break
                elif checkWin(xo) == 2:
                    print("PLAYER 2 WON")
                    break
                elif count >= 9:
                    print("MATCH DRAW")
                    break
                if isPlayer1:
                    # Player 1 input
                    ans = inputIDXPlayer(isPlayer1)
                    # VALIDATING 
                    if ans not in inputed and ans in range(1, 10):
                        count += 1
                        inputed.append(ans)
                        if ans < 4:
                            xo[0][ans - 1] = "O"
                            isPlayer1 = False
                        elif ans > 3 and ans < 7:
                            xo[1][ans - 4] = "O"
                            isPlayer1 = False
                        elif ans > 6:
                            xo[2][ans - 7] = "O"
                            isPlayer1 = False
                    else:
                        print("InValid INPUT Enter Again")
                elif not isPlayer1:
                    # Player 2 input
                    ans = inputIDXPlayer(isPlayer1)
                    # VALIDATING
                    if ans not in inputed and ans in range(1,10):
                        count += 1
                        inputed.append(ans)
                        if ans < 4:
                            xo[0][ans - 1] = "X"
                            isPlayer1 = True
                        elif ans > 3 and ans < 7:
                            xo[1][ans - 4] = "X"
                            isPlayer1 = True
                        elif ans > 6:
                            xo[2][ans - 7] = "X"
                            isPlayer1 = True
                    else:
                        print("InValid INPUT Enter Again")
playingTicTacToe()


