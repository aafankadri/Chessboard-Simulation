# utils.py

def pos_to_coords(pos):
    """Convert position like 'E4' to (4, 3) where 0-indexed"""
    col, row = pos[0].upper(), pos[1]
    return ord(col) - ord('A'), int(row) - 1

def coords_to_pos(x, y):
    """Convert (4, 3) back to 'E4'"""
    if 0 <= x < 8 and 0 <= y < 8:
        return f"{chr(x + ord('A'))}{y + 1}"
    return None

def shift(pos, dx, dy):
    """Shift position by dx, dy"""
    x, y = pos_to_coords(pos)
    return coords_to_pos(x + dx, y + dy)

def is_valid_position(pos):
    return pos is not None
