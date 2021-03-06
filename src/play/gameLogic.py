from src.other.gameObject import GameObject
from src.play.fruit import Fruit
from src.play.player import Player
from src.play.text import Text
import src.other.constants as c


class GameLogic(GameObject):

    def __init__(self, screen):
        super().__init__(screen)
        self._screen = screen
        self._fruit = Fruit(self._screen)
        self._player = Player(self._screen, self._fruit)
        self._text = Text(self._screen)
        self._lose = False

    def user_input(self):
        self._player.user_input()

    def update(self):
        self._fruit.update()
        if not self._lose:
            self._player.update()
        self._check_lose()

    def render(self):
        self._fruit.render()
        self._player.render()
        if self._lose:
            self._text.render()

    def _check_lose(self):
        segments = self._player.get_body()
        head, tail_segments = segments[0], segments[1:]

        # Check if head collides with tail segments or goes out of bounds
        head_body_collision = head in tail_segments
        head_boundary_collision = not (0 <= head[0] < c.TILE_X and 0 <= head[1] < c.TILE_Y)

        if head_body_collision or head_boundary_collision:
            self._lose = True
