from tetromino import *


class Square_tetromino(Tetrominoes):

    def __init__(self, stx, sty):
        super().__init__(stx, sty)
        self.color = SQUARE_COLOR
        self.rotated_90 = True
        self.rotated_180 = True
        self.rotated_270 = True
        self.rotated_360 = True

    def create_rectangle(self, stx, sty):
        return pygame.Rect(stx, sty, 2 * CUBE_a, 2 * CUBE_a)

    def create(self):
        square_cubes = []
        for i in range(0, 2):
            for k in range(0, 2):
                square_cubes.append(pygame.Rect(self.rectangle.x + i * CUBE_a, self.rectangle.y + k * CUBE_a, 30, 30))
        return square_cubes

    # in default self.rotatedFigure for all degrees return self. create therefore,
    # we don't have to override thise method inside Square_tetromino class
