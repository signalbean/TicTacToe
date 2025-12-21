import os
import random

WINS = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def display(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    b = [f"\033[9{4 if c=='X' else 1}m{c}\033[0m" if c in 'XO' else c for c in board]
    print(f"\n  {b[0]}  │  {b[1]}  │  {b[2]}  \n─────┼─────┼─────\n  {b[3]}  │  {b[4]}  │  {b[5]}  \n─────┼─────┼─────\n  {b[6]}  │  {b[7]}  │  {b[8]}  \n")

def winner(board, p):
    return any(all(board[i] == p for i in w) for w in WINS)

def minmax(board, max_turn, a=float('-inf'), b=float('inf')):
    if winner(board, 'O'): return 1
    if winner(board, 'X'): return -1
    moves = [i for i in range(9) if board[i] not in 'XO']
    if not moves: return 0
    
    for m in moves:
        board[m] = 'O' if max_turn else 'X'
        score = minmax(board, not max_turn, a, b)
        board[m] = str(m + 1)
        if max_turn: a = max(a, score)
        else: b = min(b, score)
        if a >= b: break
    return a if max_turn else b

def ai_move(board, diff):
    moves = [i for i in range(9) if board[i] not in 'XO']
    if diff == 'easy' or (diff == 'medium' and random.random() < 0.5):
        return random.choice(moves)
    return max(moves, key=lambda m: (board.__setitem__(m, 'O'), minmax(board, False), board.__setitem__(m, str(m + 1)))[1])
