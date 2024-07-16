from tetromino import *


class SKEW_tetromino(Tetrominoes):
    def __init__(self, stx, sty):
        super().__init__(stx, sty)
        self.color = SKEW_COLOR

    def create_rectangle(self, stx, sty):
        return pygame.Rect(stx, sty, 3 * CUBE_a, 2 * CUBE_a)

    def create(self):
        skew_cubes = []
        for i in range(0, 3):
            if i < 2:
                skew_cubes.append(pygame.Rect(self.rectangle.x + i * CUBE_a, self.rectangle.y, CUBE_a, CUBE_a))
            if i > 0:
                skew_cubes.append(pygame.Rect(self.rectangle.x + i * CUBE_a, self.rectangle.y + CUBE_a, CUBE_a, CUBE_a))
        return skew_cubes

    def figure_rotated_90(self):
        skew_cubes = []
        for i in range(0, 3):
            if i < 2:
                skew_cubes.append(pygame.Rect(self.rectangle.x + CUBE_a, self.rectangle.y + i * CUBE_a, CUBE_a, CUBE_a))
            if i > 0:
                skew_cubes.append(pygame.Rect(self.rectangle.x, self.rectangle.y + i * CUBE_a, CUBE_a, CUBE_a))
        return skew_cubes

    def figure_rotated_270(self):
        return self.figure_rotated_90()
