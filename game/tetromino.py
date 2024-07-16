import pygame
from abc import abstractmethod

CUBE_a = 30
SQUARE_COLOR = (255, 255, 0)
STRAIGHT_COLOR = (50, 255, 255)
T_COLOR = (173, 255, 47)
L_COLOR = (255, 165, 0)
SKEW_COLOR = (153, 255, 51)
screen = pygame.display.set_mode((600, 600))

COLLIDED = pygame.USEREVENT + 1
COLLIDED_event = pygame.event.Event(COLLIDED)


class Tetrominoes:

    # FOR ALL OF THEM ST_X ST_Y DEFINES LOCATION Of UPPER LEFT CUBE
    def __init__(self, stx, sty):
        self.rectangle = self.create_rectangle(stx, sty)
        self.figure = self.create()
        self.rotated_0 = True
        self.rotated_90 = False
        self.rotated_180 = False
        self.rotated_270 = False

    @abstractmethod
    def create_rectangle(self, stx, sty):
        pass

    @abstractmethod
    def create(self):
        pass

    def rotate_90(self, tetrominoes, grid):
        surface = pygame.Surface((self.rectangle.width, self.rectangle.height))
        surface = pygame.transform.rotate(surface, 90)
        self.rectangle.width, self.rectangle.height = surface.get_width(), surface.get_height()
        if not self.rectangle_touches_tetromino(tetrominoes) and not self.rectangle_touches_grid(grid):
            if self.rotated_0:
                self.rotated_0 = False
                self.rotated_90 = True
                self.figure = self.figure_rotated_90()
            elif self.rotated_90:
                self.rotated_90 = False
                self.rotated_180 = True
                self.figure = self.figure_rotated_180()
            elif self.rotated_180:
                self.rotated_180 = False
                self.rotated_270 = True
                self.figure = self.figure_rotated_270()
            elif self.rotated_270:
                self.rotated_270 = False
                self.rotated_0 = True
                self.figure = self.create()
        else:
            surface = pygame.Surface((self.rectangle.width, self.rectangle.height))
            surface = pygame.transform.rotate(surface, -90)
            self.rectangle.width, self.rectangle.height = surface.get_width(), surface.get_height()

    def rotate_180(self, tetrominoes, grid):
        surface = pygame.Surface((self.rectangle.width, self.rectangle.height))
        surface = pygame.transform.rotate(surface, 180)
        self.rectangle.width, self.rectangle.height = surface.get_width(), surface.get_height()
        if not self.rectangle_touches_tetromino(tetrominoes) and not self.rectangle_touches_grid(grid):
            if self.rotated_0:
                self.rotated_0 = False
                self.rotated_180 = True
                self.figure = self.figure_rotated_180()
            elif self.rotated_90:
                self.rotated_90 = False
                self.rotated_270 = True
                self.figure = self.figure_rotated_270()
            elif self.rotated_270:
                self.rotated_270 = False
                self.rotated_90 = True
                self.figure = self.figure_rotated_90()
            elif self.rotated_180:
                self.rotated_180 = False
                self.rotated_0 = True
                self.figure = self.create()
        else:
            surface = pygame.Surface((self.rectangle.width, self.rectangle.height))
            surface = pygame.transform.rotate(surface, -90)
            self.rectangle.width, self.rectangle.height = surface.get_width(), surface.get_height()

    def rotate_270(self, tetrominoes, grid):
        surface = pygame.Surface((self.rectangle.width, self.rectangle.height))
        surface = pygame.transform.rotate(surface, -90)
        self.rectangle.width, self.rectangle.height = surface.get_width(), surface.get_height()
        if not self.rectangle_touches_tetromino(tetrominoes) and not self.rectangle_touches_grid(grid):
            if self.rotated_0:
                self.rotated_0 = False
                self.rotated_270 = True
                self.figure = self.figure_rotated_270()
            elif self.rotated_90:
                self.rotated_90 = False
                self.rotated_0 = True
                self.figure = self.create()
            elif self.rotated_180:
                self.rotated_180 = False
                self.rotated_90 = True
                self.figure = self.figure_rotated_90()
            elif self.rotated_270:
                self.rotated_270 = False
                self.rotated_180 = True
                self.figure = self.figure_rotated_180()
        else:
            surface = pygame.Surface((self.rectangle.width, self.rectangle.height))
            surface = pygame.transform.rotate(surface, -90)
            self.rectangle.width, self.rectangle.height = surface.get_width(), surface.get_height()

    def figure_rotated_90(self):
        return self.create()

    def figure_rotated_180(self):
        return self.create()

    def figure_rotated_270(self):
        return self.create()

    def __touch_helper(self, other_cube):
        for cube in self.figure:
            if cube.colliderect(other_cube):
                return True
        return False

    def touches_tetromino(self, tetrominoes_list):
        for tetrominoe in tetrominoes_list:
            for cube in tetrominoe.figure:
                if self.__touch_helper(cube):
                    return True
        return False

    def rectangle_touches_tetromino(self, tetrominoes_list):
        for tetrominoe in tetrominoes_list:
            for cube in tetrominoe.figure:
                if self.rectangle.colliderect(cube):
                    return True
        return False

    def touches_grid(self, grid):
        for cube in grid:
            if self.__touch_helper(cube):
                return True
        return False

    def rectangle_touches_grid(self, grid):
        for cube in grid:
            if self.rectangle.colliderect(cube):
                return True
        return False

    def move(self, k, tetrominoes, grid):
        if k == pygame.K_DOWN:
            for i in self.figure:
                i.y += CUBE_a
            if self.touches_tetromino(tetrominoes) or self.touches_grid(grid):
                for i in self.figure:
                    i.y -= CUBE_a
                self.rectangle = None
                pygame.event.post(COLLIDED_event)
            else:
                if self.rectangle is not None:
                    self.rectangle.y += CUBE_a
        elif k == pygame.K_LEFT:
            for i in self.figure:
                i.x -= CUBE_a
            if self.touches_tetromino(tetrominoes) or self.touches_grid(grid):
                for i in self.figure:
                    i.x += CUBE_a
            else:
                if self.rectangle is not None:
                    self.rectangle.x -= CUBE_a

        elif k == pygame.K_RIGHT:
            for i in self.figure:
                i.x += CUBE_a
            if self.touches_tetromino(tetrominoes) or self.touches_grid(grid):
                for i in self.figure:
                    i.x -= CUBE_a
            else:
                if self.rectangle is not None:
                    self.rectangle.x += CUBE_a

    def move_down(self, tetrominoes, grid):
        for i in self.figure:
            i.y += CUBE_a
        if self.touches_tetromino(tetrominoes) or self.touches_grid(grid):
            for i in self.figure:
                i.y -= CUBE_a
            self.rectangle = None
            pygame.event.post(COLLIDED_event)
        else:
            self.rectangle.y += CUBE_a


def draw(lst, color):
    for cube in lst:
        pygame.draw.rect(screen, color, cube)
