# game.py Documentation

## Overview
Main game controller that handles user interaction, game flow, and coordinates between board display and AI logic.

## Functions

### `play_game()`
**Purpose**: Single game session that has the entire TicTacToe game experience.

**Flow**:
1. **Screen Clear & Menu Display**:
   - Clears terminal using `clear_screen()`
   - Displays centered title and boxed mode selection menu using a single multi-line print
2. **Game Setup**: 
   - Sets `is_ai_game` flag for AI games
   - Maps choice numbers to difficulty strings
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
   - 9 moves completed: Display "It's a tie!" and exit

### `main()`
**Purpose**: Application entry point that provides continuous play functionality with exception handling.

**Flow**:
1. Runs `play_game()` in infinite loop within try-catch block
2. After each game, prompts user to play again
3. If user chooses to continue ('y'):
   - Clears screen before starting next game
4. Exits cleanly with "Goodbye!" otherwise

**Exception Handling**:
- Catches KeyboardInterrupt (Ctrl+C) and EOFError at top level
- Allows graceful exit from anywhere in the application

**Input Handling**:
- Accepts integers 1-9 for board positions
- Converts to 0-8 array indices
- Validates moves are on empty positions
- Handles invalid input with "Invalid move!" message
- Play again prompt accepts 'y' (case insensitive) to continue

**AI Integration**:
- Detects when current player is 'O' in AI mode
- Calls `get_ai_move()` with board state and difficulty
- AI moves are automatic (no user input required)

**Error Handling**:
- Try-catch for invalid integer input within move validation loop
- Input validation loop until valid move entered

## Dependencies
- `utils` module: clear_screen, display_board, check_winner, get_ai_move
