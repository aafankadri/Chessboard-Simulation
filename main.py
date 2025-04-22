# main.py

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

def main():
    input_str = input("Enter piece and position (e.g., 'Queen, E4'): ").strip()
    
    try:
        piece_name, position = [x.strip() for x in input_str.split(',')]
        piece = get_piece_instance(piece_name, position)
        moves = piece.get_moves()
        print(", ".join(moves))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
