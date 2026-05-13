# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the board is full
def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main function for the Tic-Tac-Toe game
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        
        # Get player input for the move
        row, col = map(int, input(f"Player {current_player}, enter your move (row col): ").split())
        
        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue
        
        board[row][col] = current_player
        
        # Check if current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full and it's a draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the Tic-Tac-Toe game
if __name__ == "__main__":
    tic_tac_toe()
        
