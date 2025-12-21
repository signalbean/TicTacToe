# Save System

## Binary Format (.owo)

Ultra-compact 7-byte binary format for TicTacToe games:

### Structure
- **6 bytes**: Move data (48 bits)
- **1 byte**: Result only (no mode stored)

### Move Encoding
- **5 bits per move**: 1 bit player + 4 bits position
- **Player bit**: 0=X, 1=O  
- **Position**: 0-8 (board positions)
- **Capacity**: 9 moves maximum

### Metadata Byte
- **Bits 0-2**: Result (0=X, 1=O, 2=Tie)
- **Bits 3-7**: Unused

### File Format
Multiple games appended sequentially:
```
Game 1: [6 bytes moves][1 byte result]
Game 2: [6 bytes moves][1 byte result]
Game N: [6 bytes moves][1 byte result]
```

### Space Efficiency
- **Binary**: 7 bytes per game
- **JSON**: ~200-300 bytes per game  
- **Savings**: 97% smaller files

## Functions

### `save_game(moves, result, mode, filename="games.owo")`
Saves a game to binary format.

### `load_game(filename="games.owo")`
Loads all games from binary format, returns list of game dictionaries.
