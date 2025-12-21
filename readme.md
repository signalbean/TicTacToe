# TicTacToe

Smol TicTacToe implementation with AI opponents.

## Files

- `game.py` - Main game loop and player interaction
- `utils.py` - Board display, win detection, and AI logic

## Usage

```bash
python game.py
```

Choose mode:
1. PvP - Two players
2. Easy - Random AI moves
3. Medium - 50% optimal AI moves
4. Hard - Full minmax AI

## Functions

### utils.py
- `display(board)` - Shows colored board
- `winner(board, player)` - Checks win condition
- `minmax(board, max_turn)` - AI decision algorithm
- `ai_move(board, difficulty)` - Gets AI move based on difficulty

### game.py
- `play()` - Main game loop with input handling
