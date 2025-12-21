# game.py Documentation

## Overview
Main game controller that handles user interaction, game flow, and coordinates between board display and AI logic.

## Functions

### `play()`
**Purpose**: Main game loop that orchestrates the entire TicTacToe game experience.

**Flow**:
1. **Mode Selection**: Prompts user to choose between PvP (1) or AI difficulties (2-4)
2. **Game Setup**: 
   - Sets `ai_mode` flag for AI games
   - Maps mode numbers to difficulty strings
   - Initializes board with positions 1-9
   - Sets starting player to 'X'
3. **Game Loop**: Runs for maximum 9 turns
   - Displays current board state
   - Gets move from human player or AI based on current player and mode
   - Validates human input (1-9, position available)
   - Places move on board
   - Checks for winner after each move
   - Switches players (X ↔ O)
4. **End Conditions**:
   - Winner found: Display winner and exit
   - 9 moves completed: Display "Tie!"
   - User interruption: Clean exit message

**Input Handling**:
- Accepts integers 1-9 for board positions
- Converts to 0-8 array indices
- Validates moves are on empty positions
- Handles invalid input with "Invalid!" message
- Supports Ctrl+C graceful exit

**AI Integration**:
- Detects when current player is 'O' in AI mode
- Calls `ai_move()` with board state and difficulty
- AI moves are automatic (no user input required)

**Error Handling**:
- Try-catch for invalid integer input
- KeyboardInterrupt and EOFError for clean exits
- Input validation loop until valid move entered
