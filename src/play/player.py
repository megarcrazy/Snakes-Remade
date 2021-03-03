import pygame
from src.gameObject import GameObject
from src.user_input import UserInput
import src.constants as c


class Player(GameObject):

    def __init__(self, screen):
        super().__init__(screen)
        self._head = []
        self._tail = []

        self._size = 0
        self._direction = c.RIGHT
        self._initialise_player()

        self._counter = 0

    def user_input(self):
        keys = UserInput.get_keyboard()
        if keys[pygame.K_w]:
            self._direction = c.UP
        elif keys[pygame.K_s]:
            self._direction = c.DOWN
        elif keys[pygame.K_a]:
            self._direction = c.LEFT
        elif keys[pygame.K_d]:
            self._direction = c.RIGHT

    def update(self):
        if self._counter == c.SNAKE_SPEED:
            self._move_snake()
            self._counter = 0
        else:
            self._counter += 1

    def render(self):
        self._render_tail()
        self._render_head()

    def _render_head(self):
        head_rect = [
            self._head[0] * c.GRID_SIZE, self._head[1] * c.GRID_SIZE,
            c.GRID_SIZE, c.GRID_SIZE
        ]
        pygame.draw.rect(self._screen, c.SNAKE_HEAD_COLOUR, head_rect)

    def _render_tail(self):
        for tail in self._tail:
            segment_rect = [
                tail[0] * c.GRID_SIZE, tail[1] * c.GRID_SIZE,
                c.GRID_SIZE, c.GRID_SIZE
            ]
            pygame.draw.rect(self._screen, c.SNAKE_COLOUR, segment_rect)

    def _initialise_player(self):
        self._initialise_head()
        self._initialise_tail()

    def _initialise_head(self):
        x = c.SCREEN_WIDTH // (2 * c.GRID_SIZE)
        y = c.SCREEN_HEIGHT // (2 * c.GRID_SIZE)
        self._head = [x, y]
        self._size += 1

    def _initialise_tail(self):
        self._tail.append([self._head[0] - 1, self._head[1]])
        self._tail.append([self._head[0] - 2, self._head[1]])
        self._size += 2

    def _move_snake(self):
        self._tail = [list(self._head)] + self._tail[:-1]
        self._head = [
            self._head[0] + self._direction[0],
            self._head[1] + self._direction[1]
        ]
