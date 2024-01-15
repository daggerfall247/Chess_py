from .field import Field

class Move:
    def __init__(self, start : Field, end : Field):
        self.start = start
        self.end = end