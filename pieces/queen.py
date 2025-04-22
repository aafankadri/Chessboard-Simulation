# pieces/queen.py

from pieces.base import Piece
from utils import shift, is_valid_position

class Queen(Piece):
    def get_moves(self):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        moves = []

        for dx, dy in directions:
            current = self.position
            while True:
                current = shift(current, dx, dy)
                if not is_valid_position(current):
                    break
                moves.append(current)
        return moves
