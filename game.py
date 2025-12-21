from utils import display, winner, ai_move
from replay import save_game, replay_game

def play():
    try:
        moves = []
        
        print("1. PvP  2. Easy  3. Medium  4. Hard  5. Replay")
        mode = input("> ")
        
        if mode == '5':
            replay_game()
            return
            
        ai_mode = mode in '234'
        diff = {'2': 'easy', '3': 'medium', '4': 'hard'}.get(mode)
        board = [str(i) for i in range(1, 10)]
        player = 'X'
        move_num = 1
        
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
            
            moves.append({'move_num': move_num, 'player': player, 'position': move})
            board[move] = player
            move_num += 1
            
            if winner(board, player):
                display(board)
                result = f"{'AI' if player == 'O' and ai_mode else player} wins!"
                print(result)
                save_game(moves, result, mode)
                return
            player = 'O' if player == 'X' else 'X'
        
        display(board)
        result = "Tie!"
        print(result)
        save_game(moves, result, mode)
    except (KeyboardInterrupt, EOFError):
        print("\nExited.")

def main():
    while True:
        play()
        if input("\nPlay again? (y/N): ").lower() != 'y':
            print("\nExited.")
            break

if __name__ == "__main__":
    main()
