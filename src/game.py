from utils import *

def play_game():
    clear_screen()

    print("""
           Tic Tac Toe      
    ┌───────────────────────┐
    │ 1. PvP                │
    │ 2. Easy               │
    │ 3. Medium             │
    │ 4. Hard               │
    └───────────────────────┘
    """)

    choice = input("Choose mode: ")
    
    is_ai_game = choice in '234'
    difficulty = {'2': 'easy', '3': 'medium', '4': 'hard'}.get(choice)
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'
    
    for turn in range(9):
        display_board(board)
        
        if current_player == 'O' and is_ai_game:
            position = get_ai_move(board, difficulty)
        else:
            while True:
                try:
                    position = int(input(f"{current_player} choose (1-9): ")) - 1
                    if 0 <= position <= 8 and board[position] not in 'XO':
                        break
                except:
                    pass
                print("Invalid move!")
        
        board[position] = current_player
        
        if check_winner(board, current_player):
            display_board(board)
            winner_name = 'AI' if current_player == 'O' and is_ai_game else current_player
            print(f"{winner_name} wins!")
            return
            
        current_player = 'O' if current_player == 'X' else 'X'
    
    display_board(board)
    print("It's a tie!")

def main():
    try:
        while True:
            play_game()
            if input("Play again? (y/N): ").lower() != 'y':
                print("Goodbye!")
                break
            clear_screen()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

if __name__ == "__main__":
    main()
