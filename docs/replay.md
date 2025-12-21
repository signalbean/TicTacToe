# replay.py Documentation

## Overview
Game recording and replay system that saves game history and allows users to review past matches step-by-step.

## Functions

### `save_game(moves, result, mode)`
**Purpose**: Saves completed game data to persistent storage.

**Parameters**:
- `moves`: List of move dictionaries containing move_num, player, and position
- `result`: String describing game outcome ("X wins!", "O wins!", "AI wins!", "Tie!")
- `mode`: String indicating game mode ('1'-'5')

**Flow**:
1. Creates game dictionary with moves, result, and mode
2. Loads existing games from `games.json` if file exists
3. Appends new game to games list
4. Writes updated games list back to `games.json`

**Data Structure**:
```json
{
  "moves": [
    {"move_num": 1, "player": "X", "position": 4},
    {"move_num": 2, "player": "O", "position": 0}
  ],
  "result": "X wins!",
  "mode": "2"
}
```

### `replay_game()`
**Purpose**: Interactive replay system for viewing recorded games.

**Flow**:
1. **Screen Clear**: Clears terminal for clean display
2. **File Check**: Verifies `games.json` exists, exits if no games found
3. **Game Selection**: 
   - Loads all games from JSON file
   - Shows last 5 games with result and mode
   - Prompts user to select game (1-5)
4. **Replay Execution**:
   - Initializes fresh board state
   - Steps through each recorded move
   - Displays board after each move with move details
   - Waits for user input (Enter) between moves
   - Shows final result after last move

**Display Format**:
- Game list: `"1. X wins! - 2"` (number, result, mode)
- Move display: `"Move 1: X -> 5"` (move number, player, board position)
- Final display: `"Final result: X wins!"`

**Error Handling**:
- Handles missing `games.json` file
- Validates user choice is within valid range (1-5)
- Generic exception handling for invalid input
- Displays "Invalid choice!" for any input errors

**User Interaction**:
- Press Enter to advance through moves
- Step-by-step visualization of game progression
- Clean terminal display between games

## Dependencies
- `json`: For reading/writing game data
- `os`: For file operations and screen clearing
- `utils.display`: For board visualization during replay

## File Format
Games are stored in `games.json` as a JSON array of game objects, automatically created and maintained by the save system.
