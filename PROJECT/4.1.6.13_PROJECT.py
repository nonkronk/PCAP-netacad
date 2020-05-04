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
        userMove = int(input("Enter your move: "))
        if userMove not in range(1, 10):
            continue
        for i in range(3):
            for j in range(3):
                if userMove == board[i][j]:
                    board[i][j] = "O"
                    return

def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
    freeFields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "O" and board[i][j] != "X":
                freeFields.append(tuple([i, j]))
    return freeFields

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

board = [[1, 2, 3],[4, "X", 6], [7, 8, 9]]
for i in range(4):
    DisplayBoard(board)
    EnterMove(board)
    DisplayBoard(board)
    DrawMove(board)
    if VictoryFor(board, "X") == "X":
        DisplayBoard(board)
        print("You lose!")
        break
    if VictoryFor(board, "O") == "O":
        DisplayBoard(board)
        print("You won!")
        break

if VictoryFor(board, "O") == None and VictoryFor(board, "X") == None:
    DisplayBoard(board)
    print("It's a tie!")
