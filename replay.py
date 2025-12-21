import json
import os
from utils import display

def save_game(moves, result, mode):
    game = {'moves': moves, 'result': result, 'mode': mode}
    games = []
    if os.path.exists('games.json'):
        with open('games.json') as f:
            games = json.load(f)
    games.append(game)
    with open('games.json', 'w') as f:
        json.dump(games, f)

def replay_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists('games.json'):
        print("No games to replay!")
        return
    with open('games.json') as f:
        games = json.load(f)
    
    print(f"\nFound {len(games)} games:")
    recent = games[-5:]
    for i, g in enumerate(recent, 1):
        print(f"{i}. {g['result']} - {g['mode']}")
    
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
        print(f"Final result: {game['result']}")
    except:
        print("Invalid choice!")
