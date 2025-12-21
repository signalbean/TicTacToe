from save import save_game, load_game
from utils import display
import os

def replay_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    games = load_game()
    
    if not games:
        print("No games to replay!")
        return
    
    print(f"\nFound {len(games)} games:")
    recent = games[-5:]
    for i, g in enumerate(recent, 1):
        result_display = f"{g['result']} wins!" if g['result'] in ['X', 'O'] else f"{g['result']}!"
        print(f"{i}. {result_display}")
    
    try:
        choice = int(input("Replay game (1-5): ")) - 1
        if choice < 0 or choice >= len(recent):
            print("Invalid choice!")
            return
        game = recent[choice]
        board = [str(i) for i in range(1, 10)]
        
        for move_data in game['moves']:
            display(board)
            print(f"Move {move_data['move_num']}: {move_data['player']} -> {move_data['position']+1}")
            input("Press Enter...")
            board[move_data['position']] = move_data['player']
        
        display(board)
        final_result = f"{game['result']} wins!" if game['result'] in ['X', 'O'] else f"{game['result']}!"
        print(f"Final result: {final_result}")
    except:
        print("Invalid choice!")
