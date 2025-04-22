
class Piece:
    def __init__(self, position):
        self.position = position.upper()

    def get_moves(self):
        raise NotImplementedError("Subclasses must implement this method.")
