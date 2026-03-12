# Tic Tac Toe (Console Version)
# X = Human (Maximizer) | O = AI (Minimizer)

import math

# ── Step 1: Create the Board ──────────────────
# A 3x3 grid using a list. '_' means empty cell.
board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

# ── Step 2: Print the Board ───────────────────
def print_board():
    print()
    print("     0     1     2")        # column headers
    print("  +-----+-----+-----+")
    for i, row in enumerate(board):
        print(f"{i} |  {row[0]}  |  {row[1]}  |  {row[2]}  |")
        print("  +-----+-----+-----+")
    print()

# ── Step 3: Evaluation Function ───────────────
# Checks who has won and returns a score:
#   +10 → X wins (good for X)
#   -10 → O wins (good for O)
#     0 → No winner yet / Draw
def evaluate():
    # Check all 3 rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            return 10 if row[0] == 'x' else -10

    # Check all 3 columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            return 10 if board[0][col] == 'x' else -10

    # Check diagonal top-left to bottom-right
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return 10 if board[0][0] == 'x' else -10

    # Check diagonal top-right to bottom-left
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return 10 if board[0][2] == 'x' else -10

    return 0  # No winner

# ── Step 4: Check if moves are left ───────────
def moves_left():
    for row in board:
        if '_' in row:
            return True
    return False

# ── Step 5: Minimax Algorithm ─────────────────
# Tries every possible move and returns the best score.
# is_maximizing=True  → X's turn (wants highest score)
# is_maximizing=False → O's turn (wants lowest score)
def minimax(depth, is_maximizing):
    score = evaluate()

    if score == 10:  return 10   # X won
    if score == -10: return -10  # O won
    if not moves_left(): return 0  # Draw

    if is_maximizing:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == '_':
                    board[r][c] = 'x'                          # try the move
                    best = max(best, minimax(depth+1, False))  # recurse
                    board[r][c] = '_'                          # undo the move
        return best

    else:
        best = +math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == '_':
                    board[r][c] = 'o'                         # try the move
                    best = min(best, minimax(depth+1, True))  # recurse
                    board[r][c] = '_'                         # undo the move
        return best

# ── Step 6: Find Best Move for AI ─────────────
# Tries every empty cell, runs minimax, picks the lowest score (AI = minimizer)
def best_move():
    best_val = +math.inf
    move = (-1, -1)

    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board[r][c] = 'o'
                val = minimax(0, True)   # after AI moves, it's X's turn (maximizer)
                board[r][c] = '_'
                if val < best_val:       # AI wants the LOWEST score
                    best_val = val
                    move = (r, c)
    return move

# ── Step 7: Play the Game ─────────────────────
def play():
    print("=== Tic Tac Toe ===")
    print("You are X | AI is O")
    print("Enter row and col (0, 1, or 2)")

    while True:
        print_board()
        score = evaluate()

        # Check if game is over
        if score == 10:
            print("You WIN! X wins!")
            break
        elif score == -10:
            print("AI WINS! O wins!")
            break
        elif not moves_left():
            print("It's a DRAW!")
            break

        # Human turn (X)
        try:
            r = int(input("Your row: "))
            c = int(input("Your col: "))
            if board[r][c] != '_':
                print("Cell taken! Try again.")
                continue
            board[r][c] = 'x'
        except:
            print("Invalid input. Use 0, 1, or 2.")
            continue

        print_board()
        score = evaluate()

        if score == 10:
            print("You WIN! X wins!")
            break
        elif not moves_left():
            print("It's a DRAW!")
            break

        # AI turn (O)
        print("AI is thinking...")
        r, c = best_move()
        board[r][c] = 'o'
        print(f"AI played at row={r}, col={c}")

# ── Run ───────────────────────────────────────
play()