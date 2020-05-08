def DisplayBoard(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #
    print(
        f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
        """)

def EnterMove(board):
    #
    # the function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision
    #
    while True:
        try:
            userMove = int(input("Enter your move: "))
        except ValueError:
            continue
        if userMove not in range(1, 10):
            continue
        for i in range(3):
            for j in range(3):
                if userMove == board[i][j]:
                    board[i][j] = "O"
                    return

def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    #
    if sign == board[0][0] == board[0][1] == board[0][2] or \
        sign == board[1][0] == board[1][1] == board[1][2] or \
        sign == board[2][0] == board[2][1] == board[2][2] or \
        sign == board[0][0] == board[1][0] == board[2][0] or \
        sign == board[0][1] == board[1][1] == board[2][1] or \
        sign == board[0][2] == board[1][2] == board[2][2] or \
        sign == board[0][0] == board[1][1] == board[2][2] or \
        sign == board[0][2] == board[1][1] == board[2][0]:
            return sign

def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    #
    from random import randrange
    while True:
        comMove = randrange(1, 10)
        for i in range(3):
            for j in range(3):
                if board[i][j] == comMove:
                    board[i][j] = "X"
                    return

# Initialize the board
board = [[1, 2, 3],[4, "X", 6], [7, 8, 9]]

# Main tictactoe program
for i in range(4):
    DisplayBoard(board)
    EnterMove(board)
    DisplayBoard(board)
    DrawMove(board)
    # Print when the computer win
    if VictoryFor(board, "X") == "X":
        DisplayBoard(board)
        print("You lose!")
        break
    # Print when the user win
    if VictoryFor(board, "O") == "O":
        DisplayBoard(board)
        print("You won!")
        break

# Print when a tie occured
if VictoryFor(board, "O") == None and VictoryFor(board, "X") == None:
    DisplayBoard(board)
    print("It's a tie!")
