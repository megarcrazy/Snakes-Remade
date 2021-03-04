import pygame
import random
from src.gameObject import GameObject
import src.constants as c


class Fruit(GameObject):

    def __init__(self, screen):
        super().__init__(screen)
        self._screen = screen
        self._location = None

    def render(self):
        rect = [
            self._location[0] * c.GRID_SIZE, self._location[1] * c.GRID_SIZE,
            c.GRID_SIZE, c.GRID_SIZE
        ]
        pygame.draw.rect(self._screen, c.FRUIT_COLOUR, rect)

    def spawn_fruit(self, player_body):
        x = random.randint(0, c.TILE_X - 1)
        y = random.randint(0, c.TILE_Y - 1)
        while [x, y] in player_body:
            x = random.randint(0, c.TILE_X - 1)
            y = random.randint(0, c.TILE_Y - 1)
        self._location = [x, y]

    def get_location(self):
        return self._location
