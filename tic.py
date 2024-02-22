def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player {}: ".format(player)))
                col = int(input("Enter column (0, 1, or 2) for player {}: ".format(player)))
                if board[row][col] == " ":
                    break
                else:
                    print("That position is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print("Player {} wins!".format(player))
            return

        player = "O" if player == "X" else "X"

    print("It's a tie!")

tic_tac_toe()