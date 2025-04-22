# test_chess.py

import unittest
from pieces.king import King
from pieces.queen import Queen
from pieces.pawn import Pawn

class TestChessPieces(unittest.TestCase):

    def test_king_moves_center(self):
        k = King("D5")
        expected = sorted(["C4", "C5", "C6", "D4", "D6", "E4", "E5", "E6"])
        self.assertEqual(sorted(k.get_moves()), expected)

    def test_king_moves_corner(self):
        k = King("A1")
        expected = sorted(["A2", "B1", "B2"])
        self.assertEqual(sorted(k.get_moves()), expected)

    def test_queen_moves(self):
        q = Queen("E4")
        expected = sorted([
            # horizontal
            "A4", "B4", "C4", "D4", "F4", "G4", "H4",
            # vertical
            "E1", "E2", "E3", "E5", "E6", "E7", "E8",
            # diagonal ↘
            "F3", "G2", "H1",
            # diagonal ↙
            "D3", "C2", "B1",
            # diagonal ↖
            "D5", "C6", "B7", "A8",
            # diagonal ↗
            "F5", "G6", "H7"
        ])
        self.assertEqual(sorted(q.get_moves()), expected)

    def test_pawn_moves(self):
        p = Pawn("G1")
        self.assertEqual(p.get_moves(), ["G2"])

    def test_pawn_edge(self):
        p = Pawn("H8")
        self.assertEqual(p.get_moves(), [])

if __name__ == '__main__':
    unittest.main()
