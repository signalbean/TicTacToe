# game.py Documentation

## Overview
Main game controller that handles user interaction, game flow, coordinates between board display and AI logic, and manages game recording/replay functionality.

## Functions

### `play()`
**Purpose**: Single game session that orchestrates the entire TicTacToe game experience with recording.

**Flow**:
1. **Mode Selection**: Prompts user to choose between PvP (1), AI difficulties (2-4), or Replay (5)
2. **Replay Handling**: If mode 5 selected, calls `replay_game()` and returns
3. **Game Setup**: 
   - Initializes `moves` list for recording
   - Sets `ai_mode` flag for AI games
   - Maps mode numbers to difficulty strings
   - Initializes board with positions 1-9
   - Sets starting player to 'X' and move counter to 1
4. **Game Loop**: Runs for maximum 9 turns
   - Displays current board state
   - Gets move from human player or AI based on current player and mode
   - Validates human input (1-9, position available)
   - Records move data (move number, player, position)
   - Places move on board and increments move counter
   - Checks for winner after each move
   - Switches players (X ↔ O)
5. **End Conditions**:
   - Winner found: Display winner, save game, and exit
   - 9 moves completed: Display "Tie!", save game, and exit

**Game Recording**:
- Tracks each move with player, position, and move number
- Saves complete game data including result and mode
- Calls `save_game()` from replay module on game completion

### `main()`
**Purpose**: Application entry point that provides continuous play functionality with exception handling.

**Flow**:
1. Runs `play()` in infinite loop within try-catch block
2. After each game, prompts user to play again
3. Exits cleanly if user declines (anything other than 'y')
4. Handles KeyboardInterrupt and EOFError for clean exits

**Exception Handling**:
- Catches KeyboardInterrupt (Ctrl+C) and EOFError at top level
- Allows graceful exit from anywhere in the application

**Input Handling**:
- Accepts integers 1-9 for board positions
- Converts to 0-8 array indices
- Validates moves are on empty positions
- Handles invalid input with "Invalid!" message
- Play again prompt accepts 'y' (case insensitive) to continue

**AI Integration**:
- Detects when current player is 'O' in AI mode
- Calls `ai_move()` with board state and difficulty
- AI moves are automatic (no user input required)

**Error Handling**:
- Try-catch for invalid integer input within move validation loop
- Input validation loop until valid move entered

## Dependencies
- `utils` module: display, winner, ai_move functions
- `save` module: save_game function (imported via replay)
- `replay` module: replay_game function
