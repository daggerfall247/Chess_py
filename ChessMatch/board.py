from __future__ import annotations
from ChessMatch.movestrategies import Piece
from ChessMatch.pieces import Piece
from .field import Field
from .pieces import Piece, LightPiece, DarkPiece
from .movestrategies import *
from .move import Move


class Board:

    def __init__(self):
        self.fields : list[list[Field]] = self.getInitialBoard()
        self.moveStrategy : MoveStrategy = None


    def makeMove(self, move : Move) -> None:
        if not move.start.piece:
            print('first field does not contain a piece!')
            return
        
        if move.start == move.end:
            print('cannot move piece onto the same field!')
            return
        
        self.chooseStrategy(move.start.piece)

        if self.moveStrategy.isValid(self.fields, move.start):
            move.end.piece = move.start.piece
            move.start.piece = None

        else:
            print('cannot move to second field by game rules')


    def chooseStrategy(self, piece: Piece):
        match piece:
            case DarkPiece.QUEEN:
                self.moveStrategy = DarkQueenMoveStrategy()
            case DarkPiece.KING:
                self.moveStrategy = DarkKingMoveStrategy()
            case DarkPiece.KNIGHT:
                self.moveStrategy = DarkKnightMoveStrategy()
            case DarkPiece.BISHOP:
                self.moveStrategy = DarkBishopMoveStrategy()
            case DarkPiece.ROOK:
                self.moveStrategy = DarkRookMoveStrategy()
            case DarkPiece.PAWN:
                self.moveStrategy = DarkPawnMoveStrategy()

            case LightPiece.QUEEN:
                self.moveStrategy = LightQueenMoveStrategy()
            case LightPiece.KING:
                self.moveStrategy = LightKingMoveStrategy()
            case LightPiece.KNIGHT:
                self.moveStrategy = LightKnightMoveStrategy()
            case LightPiece.BISHOP:
                self.moveStrategy = LightBishopMoveStrategy()
            case LightPiece.ROOK:
                self.moveStrategy = LightRookMoveStrategy()
            case LightPiece.PAWN:
                self.moveStrategy = LightPawnMoveStrategy()

    def getInitialBoard(self) -> list[list[Field]]:
        allFields : list[list[Field]] = [[Field(chr(97+file) + str(8-rank), (file, rank), None) for file in range(8)] for rank in range(8)]

        allPieces : list[Piece] = [DarkPiece.ROOK, DarkPiece.KNIGHT, DarkPiece.BISHOP, DarkPiece.QUEEN, DarkPiece.KING, DarkPiece.BISHOP, DarkPiece.KNIGHT, DarkPiece.ROOK,
                                   DarkPiece.PAWN, DarkPiece.PAWN, DarkPiece.PAWN, DarkPiece.PAWN, DarkPiece.PAWN, DarkPiece.PAWN, DarkPiece.PAWN, DarkPiece.PAWN,
                                   LightPiece.PAWN, LightPiece.PAWN, LightPiece.PAWN, LightPiece.PAWN, LightPiece.PAWN, LightPiece.PAWN, LightPiece.PAWN, LightPiece.PAWN,
                                   LightPiece.ROOK, LightPiece.KNIGHT, LightPiece.BISHOP, LightPiece.QUEEN, LightPiece.KING, LightPiece.BISHOP, LightPiece.KNIGHT, LightPiece.ROOK]
        
        k = 0
        for j in [0,1,6,7]:
            for i in range(8):
                allFields[j][i].piece = allPieces[k * 8 + i]
            k += 1

        return allFields