import tensorflow as tf
import numpy as np
import pygame
import sys

import painter.settings as settings
from painter.board import Board


class DigitPainter:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.screen.fill(settings.BACKGROUND_COLOR)
        pygame.display.set_caption("DigitPainter")

        self.board = Board(self.screen)

        self.model = tf.keras.models.load_model('model')

    def run(self):
        while True:
            self.check_events()
            self.update_screen()
            pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_mouse_button_down_events(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.check_mouse_button_up_events(event)
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_mouse_button_down_events(self, event):
        if event.button == 1:
            self.board.set_draw_mode()

    def check_mouse_button_up_events(self, event):
        if event.button == 1:
            self.board.unset_draw_mode()

    def check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_r:
            self.board.restart()
        elif event.key == pygame.K_SPACE:
            np_array = self.board.get_image_as_np_array()
            prediction = np.argmax(self.model(np_array))
            print(f"This digit is a {prediction}")
            self.board.restart()

    def update_screen(self):
        if self.board.is_painting:
            x, y = pygame.mouse.get_pos()
            x, y = x // settings.CELL_SIZE, y // settings.CELL_SIZE
            self.board.draw_cell(x, y)


def main():
    painter = DigitPainter()
    painter.run()


if __name__ == '__main__':
    main()
