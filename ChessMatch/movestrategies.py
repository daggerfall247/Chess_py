from abc import ABC, abstractmethod

from .field import Field
from .pieces import Piece
from .move import Move

class MoveStrategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ...

class DarkKingMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans

class DarkQueenMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans

class DarkRookMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans

class DarkKnightMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans

class DarkBishopMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans

class DarkPawnMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans
    
###################################################################
    
class LightKingMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans

class LightQueenMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans

class LightRookMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans

class LightKnightMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans

class LightBishopMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans

class LightPawnMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ans = True
        return ans