# Lab 06 - Tic Tac Toe (GUI Version)
# X = Human (Maximizer) | O = AI (Minimizer)

import math
import tkinter as tk
from tkinter import messagebox

# ── Step 1: Board Setup ───────────────────────
board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

# ── Step 2: Evaluation Function ───────────────
# Returns +10 if X wins, -10 if O wins, 0 otherwise
def evaluate():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            return 10 if row[0] == 'X' else -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            return 10 if board[0][col] == 'X' else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return 10 if board[0][2] == 'X' else -10

    return 0

# ── Step 3: Check if moves are left ───────────
def moves_left():
    for row in board:
        if '_' in row:
            return True
    return False

# ── Step 4: Minimax Algorithm ─────────────────
def minimax(depth, is_maximizing):
    score = evaluate()
    if score == 10:  return 10
    if score == -10: return -10
    if not moves_left(): return 0

    if is_maximizing:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == '_':
                    board[r][c] = 'X'
                    best = max(best, minimax(depth+1, False))
                    board[r][c] = '_'
        return best
    else:
        best = +math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == '_':
                    board[r][c] = 'O'
                    best = min(best, minimax(depth+1, True))
                    board[r][c] = '_'
        return best

# ── Step 5: Find Best Move for AI ─────────────
def best_move():
    best_val = +math.inf
    move = (-1, -1)
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board[r][c] = 'O'
                val = minimax(0, True)
                board[r][c] = '_'
                if val < best_val:
                    best_val = val
                    move = (r, c)
    return move

# ── Step 6: GUI Setup ─────────────────────────
window = tk.Tk()
window.title("Tic Tac Toe - Lab 06")
window.configure(bg="#2b2b2b")

# Title label
tk.Label(window, text="Tic Tac Toe", font=("Arial", 22, "bold"),
         bg="#2b2b2b", fg="white").grid(row=0, column=0, columnspan=3, pady=10)

# Status label - shows whose turn it is
status = tk.Label(window, text="Your turn (X)", font=("Arial", 13),
                  bg="#2b2b2b", fg="#90EE90")
status.grid(row=1, column=0, columnspan=3, pady=5)

# Eval score label
eval_label = tk.Label(window, text="Eval Score: 0", font=("Arial", 11),
                      bg="#2b2b2b", fg="#aaaaaa")
eval_label.grid(row=2, column=0, columnspan=3)

# 3x3 grid of buttons
buttons = [[None]*3 for _ in range(3)]

# ── Step 7: Handle Button Click ───────────────
def on_click(r, c):
    # Ignore if cell is taken or game is over
    if board[r][c] != '_':
        return

    # Human plays X
    board[r][c] = 'X'
    buttons[r][c].config(text='X', fg='#89b4fa', state='disabled')

    # Update eval score
    eval_label.config(text=f"Eval Score: {evaluate()}")

    # Check if human won or draw
    if evaluate() == 10:
        status.config(text="You WIN! 🎉", fg="#89b4fa")
        messagebox.showinfo("Game Over", "You WIN! X wins!")
        return
    if not moves_left():
        status.config(text="It's a DRAW! 🤝")
        messagebox.showinfo("Game Over", "It's a DRAW!")
        return

    # AI plays O
    status.config(text="AI is thinking... (O)")
    window.update()

    row, col = best_move()
    board[row][col] = 'O'
    buttons[row][col].config(text='O', fg='#f38ba8', state='disabled')

    # Update eval score
    eval_label.config(text=f"Eval Score: {evaluate()}")

    # Check if AI won or draw
    if evaluate() == -10:
        status.config(text="AI WINS! 🤖", fg="#f38ba8")
        messagebox.showinfo("Game Over", "AI WINS! O wins!")
        return
    if not moves_left():
        status.config(text="It's a DRAW! 🤝")
        messagebox.showinfo("Game Over", "It's a DRAW!")
        return

    status.config(text="Your turn (X)", fg="#90EE90")

# ── Step 8: Create the 3x3 Buttons ───────────
for r in range(3):
    for c in range(3):
        btn = tk.Button(window, text='', font=("Arial", 32, "bold"),
                        width=4, height=2,
                        bg="#3c3f41", fg="white", relief="flat",
                        command=lambda r=r, c=c: on_click(r, c))
        btn.grid(row=r+3, column=c, padx=5, pady=5)
        buttons[r][c] = btn

# ── Step 9: Reset Button ──────────────────────
def reset():
    for r in range(3):
        for c in range(3):
            board[r][c] = '_'
            buttons[r][c].config(text='', state='normal', bg="#3c3f41")
    status.config(text="Your turn (X)", fg="#90EE90")
    eval_label.config(text="Eval Score: 0")

tk.Button(window, text="New Game", font=("Arial", 12, "bold"),
          bg="#4CAF50", fg="white", relief="flat", padx=15, pady=6,
          command=reset).grid(row=6, column=0, columnspan=3, pady=15)

# ── Run ───────────────────────────────────────
window.mainloop()