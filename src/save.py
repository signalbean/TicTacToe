def save_game(moves, result, mode, filename="games.owo"):
    """Save game in 7-byte binary format: 9 moves (5 bits each) + result (2 bits)"""
    move_data = 0
    for i, move in enumerate(moves):
        pos = move['position']
        player_bit = 1 if move['player'] == 'O' else 0
        # 5 bits per move: 1 bit player + 4 bits position (0-8)
        move_bits = (player_bit << 4) | pos
        move_data |= (move_bits << (i * 5))
    
    # Result: 0=X, 1=O, 2=Tie
    if "Tie" in result:
        result_code = 2
    elif "O" in result or "AI" in result:
        result_code = 1
    else:
        result_code = 0
    
    # Mode: (removed - not saved)
    
    # Result: 0=X, 1=O, 2=Tie
    
    # Pack into 7 bytes: 6 bytes moves + 1 byte result
    
    try:
        with open(filename, "ab") as f:
            f.write(move_data.to_bytes(6, 'little') + bytes([result_code]))
    except:
        with open(filename, "wb") as f:
            f.write(move_data.to_bytes(6, 'little') + bytes([result_code]))

def load_game(filename="games.owo"):
    """Load all games from binary format"""
    try:
        with open(filename, "rb") as f:
            data = f.read()
        
        games = []
        for i in range(0, len(data), 7):
            if i + 7 > len(data): break
            
            chunk = data[i:i+7]
            move_data = int.from_bytes(chunk[:6], 'little')
            result_code = chunk[6]
            
            moves = []
            for j in range(9):
                move_bits = (move_data >> (j * 5)) & 0x1F  # 5 bits
                if move_bits == 0 and j > 0: break
                pos = move_bits & 0xF  # 4 bits for position
                player = 'O' if (move_bits >> 4) & 1 else 'X'  # 1 bit for player
                if pos < 9:
                    moves.append({'move_num': j+1, 'player': player, 'position': pos})
            
            if not moves: continue  # Skip empty games
            
            result = ["X", "O", "Tie"][result_code]
            
            games.append({'moves': moves, 'result': result})
        
        return games
    except Exception as e:
        print(f"Load error: {e}")
        return []
