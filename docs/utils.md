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

### `display(board)`
**Purpose**: Renders the game board with colors and formatting

**Process**:
1. **Screen Clear**: Uses `os.system()` to clear terminal (cross-platform)
2. **Color Coding**: 
   - X: Blue (`\033[94m`)
   - O: Red (`\033[91m`)
   - Numbers: Default color
3. **Board Layout**: Creates 3x3 grid with Unicode box characters
4. **Formatting**: Spaces and separators for visual clarity

**Input**: `board` - List of 9 strings (positions 0-8)
**Output**: Formatted board printed to console

### `winner(board, player)`
**Purpose**: Checks if specified player has won the game

**Algorithm**:
- Iterates through all winning combinations in `WINS`
- For each combination, checks if all 3 positions contain the player's symbol
- Returns `True` if any winning combination is found
- Uses `any()` and `all()` for efficient checking

**Input**: 
- `board` - Current board state
- `player` - 'X' or 'O' to check for win

**Output**: Boolean indicating if player has won

### `minmax(board, max_turn, a, b)`
**Purpose**: Implements minmax algorithm with alpha-beta pruning for optimal AI moves

**Algorithm**:
1. **Base Cases**:
   - O wins: return +1 (AI victory)
   - X wins: return -1 (human victory)  
   - No moves left: return 0 (tie)

2. **Recursive Case**:
   - Generate all available moves
   - For each move, simulate placing piece
   - Recursively evaluate resulting position
   - Restore board state after evaluation
   - Apply alpha-beta pruning to cut off branches

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
- `max_turn` - Boolean, True for AI turn, False for human
- `a` - Alpha value for pruning (best maximizer score)
- `b` - Beta value for pruning (best minimizer score)

**Output**: Integer score (-1, 0, or +1)

### `ai_move(board, diff)`
**Purpose**: Selects AI move based on difficulty level

**Difficulty Levels**:
1. **Easy**: Completely random moves
2. **Medium**: 50% random, 50% optimal
3. **Hard**: Always optimal (minmax)

**Algorithm**:
1. **Get Available Moves**: Find all empty positions
2. **Apply Difficulty**:
   - Easy: `random.choice(moves)`
   - Medium: 50% chance of random move
   - Hard: Always use minimax evaluation
3. **Optimal Move Selection**:
   - Try each available move
   - Evaluate position using minmax
   - Select move with highest score
   - Uses lambda function for compact evaluation

**Input**:
- `board` - Current game state
- `diff` - Difficulty string ('easy', 'medium', 'hard')

**Output**: Integer (0-8) representing chosen move position

## Technical Notes

### Alpha-Beta Pruning
- Optimization technique for minmax
- Eliminates branches that won't affect final decision
- Significantly reduces computation time
- Maintains same result as full minmax tree

### Board State Management
- Board is modified during minmax evaluation
- Always restored to original state after evaluation
- Ensures no side effects on actual game board

### Move Representation
- Internal: 0-8 array indices
- User Interface: 1-9 position numbers
- Conversion handled in game.py input processing
