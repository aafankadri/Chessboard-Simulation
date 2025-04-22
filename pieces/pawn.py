# pieces/pawn.py

from pieces.base import Piece
from utils import shift, is_valid_position

class Pawn(Piece):
    def get_moves(self):
        move = shift(self.position, 0, 1)
        return [move] if is_valid_position(move) else []
