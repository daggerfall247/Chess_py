from .pieces import Piece

class Field:
    def __init__(self, id, coors, piece=None):
        self.id : str = id
        self.coors : tuple[int, int] = coors
        self.piece : Piece = piece

