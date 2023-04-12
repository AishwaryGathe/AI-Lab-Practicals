board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

currentPlayer = "X"
winner = None
gameRunning = True

# Printing the game board
print("{ WELCOME TO PLAY TIC TAC TOE }\n")
def printBoard(board):
    print(board[0] + "  | " + board[1] + "  | " + board[2])
    print("------------")
    print(board[3] + "  | " + board[4] + "  | " + board[5])
    print("------------")
    print(board[6] + "  | " + board[7] + "  | " + board[8])

printBoard(board)
# END-------------------------------------------------------->

# Taking Player Input
def playerInput(board):
    while True:
        num = int(input("Enter a number between 1 - 9 : "))
        if 1 <= num <= 9 and board[num - 1] == " ":
            board[num - 1] = currentPlayer
            break
        elif board[num - 1] != " ":
            print("<<<< ---- Spot is already covered ---- >>>>")
        else:
            print("Invalid input. Please enter a number between 1 - 9.")


# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7]  and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if " " not in board:
        print("|<<<<< ---- TIE ---- >>>>>|")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkHorizontle(board) or checkRow(board):
        print(f"WINNER IS {winner}")
        gameRunning = False

#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# checking for win or tie again
while gameRunning:
    playerInput(board)
    printBoard(board)
    checkWin()
    checkTie(board)
    switchPlayer()
