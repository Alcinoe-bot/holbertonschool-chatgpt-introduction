#!/usr/bin/python3

def print_board(board):
    """Print the current Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there's a winner on the board."""
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Check diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]  # Initialize the board
    player = "X"  # Start with player "X"
    
    while True:
        print_board(board)
        try:
            # Get valid input for row and column
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            # Check if the input is within bounds
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter a row and column between 0 and 2.")
                continue  # Prompt user again without changing the board

            # Check if the selected spot is available
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Make the move
            board[row][col] = player

            # Check if this player won after the move
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break  # End the game

            # Switch players
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter a valid number (0, 1, or 2).")

tic_tac_toe()
