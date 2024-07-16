import random
import time

from L_tetromino import *
from SKEW_tetromino import *
from Square_tetromino import *
from Straight_tetromino import *
from T_tetromino import *

pygame.init()
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 750
BACKGROUND_COLOR = (0, 0, 204)
CUBE_a = 30

FONT = pygame.font.SysFont("Arial", 24)
FONT2 = pygame.font.SysFont("Arial", 32)

x_BORDER = 50
y_BORDER = 80

x_distance_BOX = 450
y_distance_BOX = 250

GRID_COLOR = (238, 130, 238)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BUTTON_CONTINUE_GAME = pygame.Rect(80, 200, 4 * CUBE_a, 2 * CUBE_a)
BUTTON_COLOR = (255, 153, 255)
END_GAME_TEXT_COLOR = (255, 250, 255)

SCORE = 0
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


def grid():
    grid_lst = []
    for k in range(0, 22):
        if k == 0 or k == 21:
            for i in range(0, 12):
                grid_lst.append(pygame.Rect(x_BORDER + i * CUBE_a, y_BORDER + k * CUBE_a, CUBE_a, CUBE_a))
        else:
            grid_lst.append(pygame.Rect(x_BORDER + 0 * CUBE_a, y_BORDER + k * CUBE_a, CUBE_a, CUBE_a))
            grid_lst.append(pygame.Rect(x_BORDER + 11 * CUBE_a, y_BORDER + k * CUBE_a, CUBE_a, CUBE_a))
    return grid_lst


def grid_withou_upper():
    grid_lst = grid()
    removed = []
    for cube in grid_lst:
        if cube.y == y_BORDER:
            removed.append(cube)
    return [a for a in grid_lst if a not in removed]


def next_tetromino_box():
    box_rect = []
    for i in range(0, 7):

        if i == 0 or i == 6:
            for k in range(0, 7):
                box_rect.append(pygame.Rect(x_distance_BOX + k * CUBE_a, y_distance_BOX + i * CUBE_a, CUBE_a, CUBE_a))
        box_rect.append(pygame.Rect(x_distance_BOX, y_distance_BOX + i * CUBE_a, CUBE_a, CUBE_a))
        box_rect.append(pygame.Rect(x_distance_BOX + 7 * CUBE_a, y_distance_BOX + i * CUBE_a, CUBE_a, CUBE_a))

    return box_rect


def remove_full_line(all_cube):
    global SCORE, line
    horizontal_cubes = []
    temp = all_cube.copy()

    for pair in temp:
        same_horizon = []
        y = pair[0].y
        for p in all_cube:
            if y == p[0].y:
                same_horizon.append(p)
                temp.remove(p)

        if len(same_horizon) == 10:
            horizontal_cubes.append(same_horizon)
    SCORE += 10 * len(horizontal_cubes)
    res_all_cube = all_cube

    for horizon in horizontal_cubes:
        for pair in horizon:
            pair[1].figure.remove(pair[0])
            line = pair[0].y

        res_all_cube = [x for x in res_all_cube if x not in horizon]
        all_move_down(res_all_cube, line)  # all lines above y should go one step down
    return res_all_cube


def all_move_down(all_cube, y):
    for cube in all_cube:
        if cube[0].y < y:
            cube[0].y += CUBE_a


def draw(lst, color):
    for cube in lst:
        if cube is not None:
            pygame.draw.rect(screen, color, cube)


def draw_moving_tetromino(lst, color):
    for cube in lst:
        if cube is not None and cube.y > y_BORDER:
            pygame.draw.rect(screen, color, cube)


def random_tetromino():
    x = x_BORDER + 5 * CUBE_a
    y = y_BORDER

    ts = [Square_tetromino, Straight_tetromino, T_tetromino, L_tetromino, SKEW_tetromino]
    return random.choice(ts)(x, y)


def end_of_the_game(all_tetrominoes_cube):
    for cube in all_tetrominoes_cube:
        if cube[0].y <= y_BORDER:
            return True
    return False


def run_game():
    global SCORE
    running = True
    moving_tetromino = random_tetromino()
    next_tetromino = random_tetromino()

    interval = 0.5
    previous = time.time()
    grid_lst = grid()
    grid_lst_without_upper = grid_withou_upper()
    tetrominoes = []
    all_tetrominoes_cube = []

    next_tetr_box = next_tetromino_box()
    SCORE = 0

    while running:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                    moving_tetromino.move(event.key, tetrominoes, grid_lst_without_upper)
                elif event.key == pygame.K_d:
                    moving_tetromino.rotate_90(tetrominoes=tetrominoes, grid=grid_lst_without_upper)
                elif event.key == pygame.K_s:
                    moving_tetromino.rotate_180(tetrominoes=tetrominoes, grid=grid_lst_without_upper)
                elif event.key == pygame.K_a:
                    moving_tetromino.rotate_270(tetrominoes=tetrominoes, grid=grid_lst_without_upper)
            if event.type == COLLIDED:
                tetrominoes.append(moving_tetromino)
                for cube in moving_tetromino.figure:
                    all_tetrominoes_cube.append((cube, moving_tetromino))
                all_tetrominoes_cube = remove_full_line(all_tetrominoes_cube)
                if end_of_the_game(all_tetrominoes_cube):
                    running = False
                    game_finished = True

                    while game_finished:
                        end_game_text = FONT.render(f"If you want to Continue game click restart", False, SKEW_COLOR)
                        screen.blit(end_game_text, (BUTTON_CONTINUE_GAME.x, 100))
                        pygame.draw.rect(screen, BUTTON_COLOR, BUTTON_CONTINUE_GAME)
                        screen.blit(FONT.render("RESTART", False, SKEW_COLOR),
                                    (BUTTON_CONTINUE_GAME.x + 15, BUTTON_CONTINUE_GAME.y + 15))

                        pygame.display.update()
                        for ev in pygame.event.get():
                            if ev.type == pygame.QUIT:
                                game_finished = False
                            if ev.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = pygame.mouse.get_pos()
                                if BUTTON_CONTINUE_GAME.collidepoint(mouse_pos):
                                    game_finished = False
                                    run_game()
                else:
                    moving_tetromino = next_tetromino
                    next_tetromino = random_tetromino()

        if running:
            if time.time() - previous > interval:
                moving_tetromino.move_down(tetrominoes, grid_lst_without_upper)
                previous = time.time()

            draw_moving_tetromino(moving_tetromino.figure, moving_tetromino.color)
            for t in tetrominoes:
                draw(t.figure, t.color)

            draw(grid_lst, GRID_COLOR)
            draw(next_tetr_box, WHITE)

            next_obj = next_tetromino.__class__(next_tetromino_box()[0].x + 70, next_tetromino_box()[0].y + 80)
            draw(next_obj.figure, next_obj.color)

            screen.blit(FONT.render(f"SCORE : {SCORE}", False, YELLOW), (x_distance_BOX, y_BORDER))
            screen.blit(FONT2.render(f"NEXT", False, WHITE), (x_distance_BOX, y_distance_BOX-50))

            pygame.display.update()


if __name__ == "__main__":
    run_game()
