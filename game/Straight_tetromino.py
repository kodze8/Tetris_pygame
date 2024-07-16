from tetromino import *


class Straight_tetromino(Tetrominoes):
    def __init__(self, stx, sty):
        super().__init__(stx, sty)
        self.color = STRAIGHT_COLOR

    def create(self):
        straight_cubes = []
        for i in range(0, 4):
            straight_cubes.append(pygame.Rect(self.rectangle.x + i * CUBE_a, self.rectangle.y, CUBE_a, CUBE_a))
        return straight_cubes

    def create_rectangle(self, stx, sty):
        return pygame.Rect(stx, sty, 4 * CUBE_a, CUBE_a)

    def figure_rotated_90(self):
        straight_cubes = []
        for i in range(0, 4):
            straight_cubes.append(pygame.Rect(self.rectangle.x, self.rectangle.y + i * CUBE_a, CUBE_a, CUBE_a))
        return straight_cubes

    def figure_rotated_180(self):
        return self.create()

    def figure_rotated_270(self):
        return self.figure_rotated_90()
