import pygame

from ChessGUI.renderer import Renderer

import ChessMatch

class Application:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.match = ChessMatch.match.Match()
        self.renderer = Renderer(self.width, self.height, self.match.board)

        pygame.init()
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        print(type(self.match.board.fields[0][0].piece))
        running = True
        start : ChessMatch.field.Field = None
        while running:
        
            self.renderer.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    field : ChessMatch.field.Field = self.getFieldFromCursorpos()
                    print(f"selected field {field.id}")
                    if start:
                        print(f'we try to move from {start.id} to {field.id}')
                        self.match.board.makeMove(ChessMatch.Move(start, field))
                        start = None
                        self.renderer.removeAttachment()

                    elif field.piece:
                        print(f'there is {field.piece} on field {field.id}, so it is remembered')
                        start = field
                        self.renderer.attachToCursor(start.piece)

                    else:
                        print(f'there is no piece on field {field.id}')

            pygame.display.flip()
            self.clock.tick(144)



        pygame.quit()

    def getFieldFromCursorpos(self):
        pos = pygame.mouse.get_pos()
        return self.match.board.fields[pos[1]//int(self.height/8)][pos[0]//int(self.width/8)]