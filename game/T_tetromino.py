from tetromino import *


class T_tetromino(Tetrominoes):

    def __init__(self, stx_x, st_y):
        super().__init__(stx_x, st_y)
        self.color = L_COLOR

    def create_rectangle(self, stx, sty):
        return pygame.Rect(stx, sty, 3 * CUBE_a, 2 * CUBE_a)

    def create(self):
        t_cubes = []
        for i in range(0, 3):
            t_cubes.append(pygame.Rect(self.rectangle.x + i * CUBE_a, self.rectangle.y, CUBE_a, CUBE_a))
            if i == 1:
                t_cubes.append(pygame.Rect(self.rectangle.x + i * CUBE_a, self.rectangle.y + CUBE_a, CUBE_a, CUBE_a))
        return t_cubes

    def figure_rotated_90(self):
        t_cubes = []
        for i in range(0, 3):
            t_cubes.append(pygame.Rect(self.rectangle.x, self.rectangle.y + i * CUBE_a, CUBE_a, CUBE_a))
            if i == 1:
                t_cubes.append(
                    pygame.Rect(self.rectangle.x + CUBE_a, self.rectangle.y + i * CUBE_a, CUBE_a, CUBE_a))
        return t_cubes

    def figure_rotated_180(self):
        t_cubes = []
        for i in range(0, 3):
            t_cubes.append(pygame.Rect(self.rectangle.x + i * CUBE_a, self.rectangle.y + CUBE_a, CUBE_a, CUBE_a))
            if i == 1:
                t_cubes.append(
                    pygame.Rect(self.rectangle.x + i * CUBE_a, self.rectangle.y, CUBE_a, CUBE_a))
        return t_cubes

    def figure_rotated_270(self):
        t_cubes = []
        for i in range(0, 3):
            t_cubes.append(pygame.Rect(self.rectangle.x + CUBE_a, self.rectangle.y + i * CUBE_a, CUBE_a, CUBE_a))
            if i == 1:
                t_cubes.append(
                    pygame.Rect(self.rectangle.x, self.rectangle.y + i * CUBE_a, CUBE_a, CUBE_a))
        return t_cubes
