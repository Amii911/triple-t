board = [ "_" , "_", "_",
          "_" , "_", "_",
          "_",  "_", "_"]

currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])

def playerInput(board):
    move = int(input("Enter a number 1-9: "))
    if move >= 1 and move <= 9 and board[move-1] == "_":
        board[move-1] == currentPlayer
    else:
        print("Choose another number, that number was already chosen")