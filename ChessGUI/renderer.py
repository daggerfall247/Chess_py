import pygame

import ChessMatch.board
import ChessMatch.pieces

class Renderer:

    def __init__(self, width, height):

        self.width : int = width
        self.height : int = height

        self.attachedSurface : pygame.Surface = None

        self.screen : pygame.Surface = pygame.display.set_mode((self.width, self.height))

        self.lightQueenSurface : pygame.Surface = self.loadIcons("img/png/lq100.png")
        self.lightKingSurface : pygame.Surface = self.loadIcons("img/png/lk100.png")
        self.lightRookSurface : pygame.Surface = self.loadIcons("img/png/lr100.png")
        self.lightKnightSurface : pygame.Surface = self.loadIcons("img/png/ln100.png")
        self.lightBishopSurface : pygame.Surface = self.loadIcons("img/png/lb100.png")
        self.lightPawnSurface : pygame.Surface = self.loadIcons("img/png/lp100.png")
        self.darkQueenSurface : pygame.Surface = self.loadIcons("img/png/dq100.png")
        self.darkKingSurface : pygame.Surface = self.loadIcons("img/png/dk100.png")
        self.darkRookSurface : pygame.Surface = self.loadIcons("img/png/dr100.png")
        self.darkKnightSurface : pygame.Surface = self.loadIcons("img/png/dn100.png")
        self.darkBishopSurface : pygame.Surface = self.loadIcons("img/png/db100.png")
        self.darkPawnSurface : pygame.Surface = self.loadIcons("img/png/dp100.png")

        self.boardSurface : pygame.Surface = self.getBoardSurface()

    def update(self, fields : list[list[ChessMatch.Field]]):
        self.screen.blit(self.boardSurface, (0,0))
        for y in range(8):
            for x in range(8):
                if fields[y][x].piece:
                    self.screen.blit(self.getSurface(fields[y][x].piece), (int(x*self.width/8), int(y*self.height/8)))

        if self.attachedSurface:
            x, y = pygame.mouse.get_pos()
            self.screen.blit(self.attachedSurface, (x - int(self.width/16), y - int(self.width/16)))

    def attachToCursor(self, piece : ChessMatch.Piece) -> None:
        self.attachedSurface = self.getSurface(piece)
        print(f'attached {piece} to cursor!')

    def removeAttachment(self) -> None:
        self.attachedSurface = None

    def loadIcons(self, filename) -> pygame.Surface :
        return pygame.image.load(filename).convert_alpha()

    def getSurface(self, piece : ChessMatch.pieces.Piece) -> pygame.Surface:
        match piece:
            case ChessMatch.LightPiece.QUEEN:
                return self.lightQueenSurface
            case ChessMatch.LightPiece.KING:
                return self.lightKingSurface
            case ChessMatch.LightPiece.KNIGHT:
                return self.lightKnightSurface
            case ChessMatch.LightPiece.BISHOP:
                return self.lightBishopSurface
            case ChessMatch.LightPiece.ROOK:
                return self.lightRookSurface
            case ChessMatch.LightPiece.PAWN:
                return self.lightPawnSurface
            
            case ChessMatch.DarkPiece.QUEEN:
                return self.darkQueenSurface
            case ChessMatch.DarkPiece.KING:
                return self.darkKingSurface
            case ChessMatch.DarkPiece.KNIGHT:
                return self.darkKnightSurface
            case ChessMatch.DarkPiece.BISHOP:
                return self.darkBishopSurface
            case ChessMatch.DarkPiece.ROOK:
                return self.darkRookSurface
            case ChessMatch.DarkPiece.PAWN:
                return self.darkPawnSurface

    def getBoardSurface(self) -> pygame.Surface :
        lightcoors : list[tuple[int, int]] = [(0,0), (200,0), (400,0), (600,0),
                                              (100,100), (300,100), (500,100), (700,100),
                                              (0,200), (200,200), (400,200), (600,200),
                                              (100,300), (300,300), (500,300), (700,300),
                                              (0,400), (200,400), (400,400), (600,400),
                                              (100,500), (300,500), (500,500), (700,500),
                                              (0,600), (200,600), (400,600), (600,600),
                                              (100,700), (300,700), (500,700), (700,700)]
        
        darkcoors : list[tuple[int, int]] = [(100,0), (300,0), (500,0), (700,0),
                                             (0,100), (200,100), (400,100), (600,100),
                                             (100,200), (300,200), (500,200), (700,200),
                                             (0,300), (200,300), (400,300), (600,300),
                                             (100,400), (300,400), (500,400), (700,400),
                                             (0,500), (200,500), (400,500), (600,500),
                                             (100,600), (300,600), (500,600), (700,600),
                                             (0,700), (200,700), (400,700), (600,700)]
        
        surface : pygame.Surface = pygame.Surface((self.width, self.width))

        for coor in lightcoors:
            pygame.draw.rect(surface, (220,220,200), pygame.Rect(coor,(self.width/8, self.width/8)))

        for coor in darkcoors:
            pygame.draw.rect(surface, (139,139,0), pygame.Rect(coor,(self.width/8, self.width/8)))

        return surface