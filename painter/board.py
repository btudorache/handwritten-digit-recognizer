import pygame
import numpy as np

import painter.settings as settings


class Cell:
    def __init__(self, dimension, x_coord, y_coord):
        self.dimension = dimension
        self.x = x_coord
        self.y = y_coord

        self.rect = pygame.Rect(self.x, self.y, self.dimension, self.dimension)
        self.color = settings.DEFAULT_COLOR

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def set_color(self, color):
        self.color = color


class Board:
    def __init__(self, screen):
        self.board_width = settings.SCREEN_WIDTH
        self.board_height = settings.SCREEN_HEIGHT
        self.cell_size = settings.CELL_SIZE

        self.screen = screen
        self.is_painting = False
        self.cells = []
        self.reset_board()

    def reset_board(self):
        self.cells = []
        for x in range(0, self.board_width, self.cell_size):
            cell_row = []
            for y in range(0, self.board_height, self.cell_size):
                cell = Cell(self.cell_size, x, y)
                cell_row.append(cell)

            self.cells.append(cell_row)

    def set_draw_mode(self):
        self.is_painting = True

    def unset_draw_mode(self):
        self.is_painting = False

    def draw_board(self):
        for cell_row in self.cells:
            for cell in cell_row:
                cell.draw(self.screen)

    def draw_cell(self, x, y):
        cell = self.cells[x][y]
        cell.set_color(settings.PAINT_COLOR)
        cell.draw(self.screen)

    def restart(self):
        self.reset_board()
        self.draw_board()

    def get_image_as_np_array(self):
        matrix = []
        for y in range(settings.HEIGHT_CELL_NUMBER):
            row = []
            for x in range(settings.WIDTH_CELL_NUMBER):
                cell = self.cells[x][y]
                if cell.color == settings.DEFAULT_COLOR:
                    row.append(0)
                elif cell.color == settings.PAINT_COLOR:
                    row.append(1)
            matrix.append(row)

        np_array = np.array(matrix)
        np_array.resize((1, settings.HEIGHT_CELL_NUMBER, settings.WIDTH_CELL_NUMBER, 1))
        return np_array
