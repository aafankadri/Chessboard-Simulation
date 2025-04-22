# pieces/king.py

from pieces.base import Piece
from utils import shift, is_valid_position

class King(Piece):
    def get_moves(self):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        possible_moves = [shift(self.position, dx, dy) for dx, dy in directions]
        return [move for move in possible_moves if is_valid_position(move)]
