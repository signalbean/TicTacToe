# utils.py Documentation

## Overview
Core utility functions for board management, game logic, and AI decision making. Contains all the mathematical and display logic.

## Constants

### `WINS`
```python
[(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
```
**Purpose**: Defines all 8 possible winning combinations on a 3x3 grid
- Rows: (0,1,2), (3,4,5), (6,7,8)
- Columns: (0,3,6), (1,4,7), (2,5,8)  
- Diagonals: (0,4,8), (2,4,6)

## Functions

### `clear_screen()`
**Purpose**: Clears the terminal screen in a cross-platform way

**Implementation**:
- Uses `os.system('cls')` on Windows
- Uses `os.system('clear')` on Unix-based systems

**Used by**:
- `display_board()`
- `game.py` menu rendering
- Between consecutive games

### `display_board(board)`
**Purpose**: Renders the game board with colors and formatting in a single compact print statement

**Process**:
1. **Screen Clear**:
   - Calls `clear_screen()` utility for reuse and consistency
2. **ANSI Color Dictionary**: 
   - `colors['X']`: Green (`\033[92m`)
   - `colors['O']`: Red (`\033[91m`)
   - `colors['reset']`: Reset color (`\033[0m`)
3. **Color Application**: One-line list comprehension maps X/O to colors, leaves numbers unchanged
4. **Single Print**: Uses f-string with embedded newlines for complete board layout
5. **Board Layout**: Creates 3x3 grid with Unicode box characters

**Input**: `board` - List of 9 strings (positions 0-8)
**Output**: Formatted board printed to console

### `check_winner(board, player)`
**Purpose**: Checks if specified player has won the game

**Algorithm**:
- Single line with `any()` and `all()` to check all winning combinations
- Iterates through all combinations in `WINS`
- Returns `True` if any winning combination is found

**Input**: 
- `board` - Current board state
- `player` - 'X' or 'O' to check for win

**Output**: Boolean indicating if player has won

### `minimax(board, is_maximizing, alpha, beta)`
**Purpose**: Implements minimax algorithm with alpha-beta pruning for optimal AI moves

**Algorithm**:
1. **Base Cases**:
   - O wins: return +1 (AI victory)
   - X wins: return -1 (human victory)  
   - No moves left: return 0 (tie)

2. **Recursive Case**:
   - Generate all available moves with list comprehension
   - For each move, simulate placing piece
   - Recursively evaluate resulting position
   - Restore board state after evaluation
   - Apply alpha-beta pruning with compact if/else

3. **Maximizing Turn** (AI's turn):
   - Tries to maximize score
   - Updates alpha value
   - Prunes when alpha >= beta

4. **Minimizing Turn** (Human's turn):
   - Tries to minimize score  
   - Updates beta value
   - Prunes when alpha >= beta

**Parameters**:
- `board` - Current game state
- `is_maximizing` - Boolean, True for AI turn, False for human
- `alpha` - Alpha value for pruning (best maximizer score)
- `beta` - Beta value for pruning (best minimizer score)

**Output**: Integer score (-1, 0, or +1)

### `get_ai_move(board, difficulty)`
**Purpose**: Selects AI move based on difficulty level using compact lambda implementation

**Difficulty Levels**:
1. **Easy**: Completely random moves
2. **Medium**: 50% random, 50% optimal
3. **Hard**: Always optimal (minimax)

**Algorithm**:
1. **Get Available Moves**: List comprehension finds all empty positions
2. **Apply Difficulty**:
   - Easy: `random.choice(moves)`
   - Medium: 50% chance of random move
   - Hard: Always use minimax evaluation
3. **Optimal Move Selection**:
   - Uses `max()` with lambda function for compact evaluation
   - Lambda uses tuple unpacking with `__setitem__` for side-effect evaluation
   - Evaluates each move using minimax and selects highest scoring

**Input**:
- `board` - Current game state
- `difficulty` - Difficulty string ('easy', 'medium', 'hard')

**Output**: Integer (0-8) representing chosen move position

## Technical Notes

### Compact Code Style
- One-line list comprehensions for data processing
- Single print statement for board display
- Lambda functions for complex evaluations
- Compact if/else statements and variable names

### Alpha-Beta Pruning
- Optimization technique for minimax
- Eliminates branches that won't affect final decision
- Significantly reduces computation time
- Maintains same result as full minimax tree

### Board State Management
- Board is modified during minimax evaluation
- Always restored to original state after evaluation
- Ensures no side effects on actual game board

### Move Representation
- Internal: 0-8 array indices
- User Interface: 1-9 position numbers
- Conversion handled in game.py input processing
