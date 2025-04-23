# main.py
import re

from pieces.king import King
from pieces.queen import Queen
from pieces.pawn import Pawn

def get_piece_instance(piece_name, position):
    piece_name = piece_name.lower()
    if piece_name == "king":
        return King(position)
    elif piece_name == "queen":
        return Queen(position)
    elif piece_name == "pawn":
        return Pawn(position)
    else:
        raise ValueError("Invalid piece type.")

VALID_PIECES = {"king", "queen", "pawn"}

def is_valid_input(piece, position):
    piece = piece.lower()
    position = position.upper()
    if piece not in VALID_PIECES:
        print("❌ Invalid piece type. Choose from: King, Queen, Pawn.")
        return False
    if not re.match(r"^[A-H][1-8]$", position):
        print("❌ Invalid position. Use format like E4 (A–H and 1–8).")
        return False
    return True

def main():
    input_str = input("Enter piece and position (e.g., 'Queen, E4'): ").strip()

    try:
        piece_name, position = [x.strip() for x in input_str.split(',')]
        
        if not is_valid_input(piece_name, position):
            return
        
        piece = get_piece_instance(piece_name, position)
        moves = piece.get_moves()
        
        print("✅ Possible Moves:")
        print(", ".join(moves) if moves else "No valid moves.")

    except ValueError:
        print("❌ Please enter input in the format: 'Piece, Position' (e.g., 'Queen, D5').")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
