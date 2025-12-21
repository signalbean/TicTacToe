# replay.py Documentation

## Overview
Game recording and replay system from the binary (.owo) savefile.

## Functions

### `replay_game()`
**Purpose**: Interactive replay system for viewing recorded games from binary format.

**Flow**:
1. **Screen Clear**: Clears terminal for clean display
2. **Load Games**: Uses `load_game()` from save.py to read binary data
3. **Game Selection**: 
   - Shows last 5 games with formatted results
   - Prompts user to select game (1-5)
4. **Replay Execution**:
   - Initializes fresh board state
   - Steps through each recorded move
   - Displays board after each move with move details
   - Waits for user input (Enter) between moves

**Display Format**:
- Game list: `"1. X wins!"` (number, formatted result)
- Move display: `"Move 1: X -> 5"` (move number, player, board position)
- Final display: `"Final result: X wins!"`

**Error Handling**:
- Validates user choice is within valid range (1-5)
- Generic exception handling for invalid input
- Displays "Invalid choice!" for any input errors

**User Interaction**:
- Press Enter to advance through moves
- Step-by-step visualization of game progression
- Clean terminal display between games

## Dependencies
- `save`: For loading games from binary format (`load_game()`)
- `utils.display`: For board visualization during replay
- `os`: For screen clearing operations

## File Format
Games are stored in `games.owo` using 7-byte binary format:
- 6 bytes: Compressed move data (5 bits per move, supports 9 moves)
- 1 byte: Result only (no mode stored)
- Multiple games appended sequentially
- Automatic file creation and maintenance
