'''board = [" "] * 9
current_player = "X"

def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def make_move(board, position, player):
    if board[position] == " ":
        board[position] = player
        return True
    return False

def check_winner(board, player):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw(board):
    return " " not in board

while True:
    print_board(board)
    move = int(input(f"Player {current_player}, choose (0-8): "))

    if not make_move(board, move, current_player):
        print("Invalid move, try again!")
        continue

    if check_winner(board, current_player):
        print_board(board)
        print(f"🎉 Player {current_player} wins!")
        break

    if is_draw(board):
        print_board(board)
        print("🤝 It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"  '''


# Tic-Tac-Toe Game in Python (Console)

board = [" "] * 9
current_player = "X"

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def make_move(position):
    if board[position] == " ":
        board[position] = current_player
        return True
    return False

def check_winner(player):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

print("🎮 Welcome to Tic-Tac-Toe!")
print("Positions are numbered 0 to 8 as shown below:")

print("""
0 | 1 | 2
--+---+--
3 | 4 | 5
--+---+--
6 | 7 | 8
""")

while True:
    print_board()

    try:
        move = int(input(f"Player {current_player}, choose position (0-8): "))
        if move < 0 or move > 8:
            print("❌ Invalid position. Choose 0-8.")
            continue
    except ValueError:
        print("❌ Please enter a number.")
        continue

    if not make_move(move):
        print("❌ Position already taken.")
        continue

    if check_winner(current_player):
        print_board()
        print(f"🏆 Player {current_player} wins!")
        break

    if is_draw():
        print_board()
        print("🤝 It's a draw!")
        break

    switch_player()
