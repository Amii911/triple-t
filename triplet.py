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