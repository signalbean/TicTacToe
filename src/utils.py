from os import system, name
from random import random, choice

WINS = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board):
    colors = {'X': '\033[92m', 'O': '\033[91m', 'reset': '\033[0m'}
    clear_screen()
    b = [f"{colors[c]}{c}{colors['reset']}" if c in 'XO' else c for c in board]
    print(f"\n  {b[0]}  │  {b[1]}  │  {b[2]}  \n─────┼─────┼─────\n  {b[3]}  │  {b[4]}  │  {b[5]}  \n─────┼─────┼─────\n  {b[6]}  │  {b[7]}  │  {b[8]}  \n")

def check_winner(board, player):
    return any(all(board[i] == player for i in w) for w in WINS)

def minimax(board, is_maximizing, alpha=float('-inf'), beta=float('inf')):
    if check_winner(board, 'O'): return 1
    if check_winner(board, 'X'): return -1
    moves = [i for i in range(9) if board[i] not in 'XO']
    if not moves: return 0
    
    for m in moves:
        board[m] = 'O' if is_maximizing else 'X'
        score = minimax(board, not is_maximizing, alpha, beta)
        board[m] = str(m + 1)
        if is_maximizing: alpha = max(alpha, score)
        else: beta = min(beta, score)
        if alpha >= beta: break
    return alpha if is_maximizing else beta

def get_ai_move(board, difficulty):
    moves = [i for i in range(9) if board[i] not in 'XO']
    if difficulty == 'easy' or (difficulty == 'medium' and random.random() < 0.5):
        return random.choice(moves)
    return max(moves, key=lambda m: (board.__setitem__(m, 'O'), minimax(board, False), board.__setitem__(m, str(m + 1)))[1])
