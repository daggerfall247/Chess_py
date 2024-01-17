from abc import ABC, abstractmethod

import math

from .field import Field
from .pieces import Piece, LightPiece, DarkPiece
from .move import Move

class MoveStrategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        ...

#######################################################

class KingMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        # TODO: check for Checks: dont allow a forbidden moves. and Castling
        if not isPotentialKingMove(move.start.coors, move.end.coors):
            return False
        
        if not move.end.piece or (move.end.piece and not type(move.end.piece) == type(move.start.piece)):
            return True
        
        return False

class QueenMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        if isPotentialQueenMove(move.start.coors, move.end.coors) and hasNoCollision(fields, move):
            return True
        else:
            return False

class RookMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        if isPotentialRookMove(move.start.coors, move.end.coors) and hasNoCollision(fields, move):
            return True
        else:
            return False
        
class KnightMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        if not isPotentialKnightMove(move.start.coors, move.end.coors):
            return False

        if not move.end.piece or (move.end.piece and not type(move.end.piece) == type(move.start.piece)):
            return True
        
        return False

class BishopMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        if isPotentialBishopMove(move.start.coors, move.end.coors) and hasNoCollision(fields, move):
            return True
        else:
            return False

class PawnMoveStrategy(MoveStrategy):
    def __init__(self):
        pass

    def isValid(self, fields : list[list[Field]], move : Move) -> bool:
        # TODO: En passant
        ydir : int
        if isinstance(move.start.piece, LightPiece):
            ydir = -1
        else:
            ydir = 1

        if not isPotentialPawnMove(move.start.coors, move.end.coors, ydir):
            return False
        
        if (move.start.coors[0] == move.end.coors[0] and not move.end.piece) or (move.start.coors[0] != move.end.coors[0] and move.end.piece and not type(move.end.piece) == type(move.start.piece)):
            return True

        return False
    
###################################################################
def isPotentialKingMove(start : tuple[int, int], finish : tuple[int, int]) -> bool:
    '''returns true if the move is a potential kings move'''
    return (abs(finish[0] - start[0]) <= 1 and abs(finish[1] - start[1]) <= 1)

def isPotentialQueenMove(start : tuple[int, int], finish : tuple[int, int]) -> bool:
    '''returns true if the move is a potential queen move'''
    return isPotentialDiagonalMove(start, finish) or isPotentialOrthogonalMove(start, finish)

def isPotentialRookMove(start : tuple[int, int], finish : tuple[int, int]) -> bool:
    '''returns true if the move is a potential rook move'''
    return isPotentialOrthogonalMove(start, finish)

def isPotentialBishopMove(start : tuple[int, int], finish : tuple[int, int]) -> bool:
    '''returns true if the move is a potential bishop move'''
    return isPotentialDiagonalMove(start, finish)

def isPotentialKnightMove(start : tuple[int, int], finish : tuple[int, int]) -> bool:
    '''returns true if the move is a potential knight move'''
    diffs = {(1,2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1)}
    for diff in diffs:
        if start[0] + diff[0] == finish[0] and start[1] + diff[1] == finish[1]:
            return True
        
    return False

def isPotentialPawnMove(start, finish, ydir) -> bool:
    '''returns true if the move is a potential pawn move'''
    diffs = {(1,ydir), (0,ydir), (-1,ydir)}
    if start[1] == 6 or start[1] == 1:
        diffs.add((0,2*ydir))

    for diff in diffs:
        if start[0] + diff[0] == finish[0] and start[1] + diff[1] == finish[1]:
            return True
        
    return False

################################################################

def isPotentialDiagonalMove(start : tuple[int, int], finish : tuple[int, int]) -> bool:
    '''returns true if start and finish share a diagonal'''
    return abs(finish[0] - start[0]) == abs(finish[1] - start[1])

def isPotentialOrthogonalMove(start : tuple[int, int], finish : tuple[int, int]) -> bool:
    '''returns true if start and finish share a rank or file'''
    return finish[0] == start[0] or finish[1] == start[1]

###############################################################

def hasNoCollision(fields : list[list[Field]], move : Move):
    '''returns true if there is no collision between start and finish for longrange moves'''
    xs : int = move.start.coors[0]
    ys : int = move.start.coors[1]
    xf : int = move.end.coors[0]
    yf : int = move.end.coors[1]
    xsign : int = sign(xf - xs)
    ysign : int = sign(yf - ys)

    x, y = xs, ys
    while x != xf or y != yf:
        x = x + xsign
        y = y + ysign
        if ((x != xf or y != yf) and fields[y][x].piece) \
        or ((x == xf and y == yf) and move.end.piece and type(move.end.piece) == type(move.start.piece)):
            return False
        
    return True

#########################################################

def sign(x : int) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0