import numpy as np

## Board Logic
## Rows are labeled 1, 2, 3
## Columns are labeled A, B, C

## Board
game_run = True
board = np.zeros((3, 3))
# Squares
squares = {"A1" : board[0][0], "A2" : board[0][1], "A3" : board[0][2], "B1" : board[1][0], "B2" : board[1][1],
           "B3" : board[1][2], "C1" : board[2][0], "C2" : board[2][1], "C3" : board[2][2]}


## Player Logic
## Human = True, Computer = False
## Human Circle is 1 in an array, 0 in an array is Empty, 2 in an array is Computer
human = True

## Player Input (In Basic Version, Player Always O)
def player_input():
    global game_run
    if not game_run:
        return
    square = input("Choose a square: ")
    if square in squares.keys():
        if squares.get(square) == 0:
            print(squares.get(square))
            board_update(square, "human")
            if game_run:
                computer_input()
        else:
            print("That square is already taken. Choose another square.")
            player_input()
    else:
        print("That square does not exist. Please type carefully!")
        player_input()

def computer_input():
    global game_run
    if not game_run:
        return
    square = np.random.choice(list(squares.keys()))
    if squares.get(square) == 0:
        board_update(square, "computer")
        if game_run:
            player_input()
    else:
        computer_input()

def board_print():
    display_board = np.empty((3, 3), dtype='U1')
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                display_board[i][j] = "-"
            if board[i][j] == 1:
                display_board[i][j] = "X"
            if board[i][j] == 2:
                display_board[i][j] = "O"
    print(display_board)


def board_update(square, player):
    row = int(list(squares.keys()).index(square) // 3)
    col = int(list(squares.keys()).index(square) % 3)

    if player == "human":
        board[row][col] = 1
        print(f"You chose {square}! Now lets look at the board.")
    else:
        board[row][col] = 2
        print(f"The Computer chose {square}! Now lets look at the board.")
    squares[square] = board[row][col]

    board_print()
    win_check()

def win_check():
    global game_run
    ## Win By Rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            if board[i][0] == 1:
                print("You Win!")
                game_run = False
            else:
                print("The Computer Wins!")
                game_run = False
            return

    ## Win By Columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            if board[0][i] == 1:
                print("You Win!")
                game_run = False
            else:
                print("The Computer Wins!")
                game_run = False
            return

    ## Win By Diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        if board[0][0] == 1:
            print("You Win!")
            game_run = False
        else:
            print("The Computer Wins!")
            game_run = False
        return

    if board[0][2] == board[1][1] == board[2][0] != 0:
        if board[0][2] == 1:
            print("You Win!")
            game_run = False
        else:
            print("The Computer Wins!")
            game_run = False
        return

    if not any(0 in row for row in board):
        print("It's a Tie!")
        game_run = False
        return


def main():
    while game_run:
        computer_input()

if __name__ == "__main__":
    main()