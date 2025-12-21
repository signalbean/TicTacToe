from utils import display, winner, ai_move

def play():
    try:
        print("1. PvP  2. Easy  3. Medium  4. Hard")
        mode = input("> ")
        ai_mode = mode in '234'
        diff = {'2': 'easy', '3': 'medium', '4': 'hard'}.get(mode)
        board = [str(i) for i in range(1, 10)]
        player = 'X'
        
        for _ in range(9):
            display(board)
            if player == 'O' and ai_mode:
                move = ai_move(board, diff)
            else:
                while True:
                    try:
                        move = int(input(f"{player} (1-9): ")) - 1
                        if 0 <= move <= 8 and board[move] not in 'XO': break
                    except: pass
                    print("Invalid!")
            
            board[move] = player
            if winner(board, player):
                display(board)
                print(f"{'AI' if player == 'O' and ai_mode else player} wins!")
                return
            player = 'O' if player == 'X' else 'X'
        
        display(board)
        print("Tie!")
    except (KeyboardInterrupt, EOFError):
        print("\nExited.")

if __name__ == "__main__":
    play()
