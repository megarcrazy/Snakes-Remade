from src.sceneManager import SceneManager
from src.play.grid import Grid
from src.play.fruit import Fruit
from src.play.player import Player
import src.constants as c


class Play(SceneManager):

    def __init__(self, screen):
        super().__init__(screen)
        self._scene_index = c.PLAY_SCENE_INDEX

        self._grid = Grid(self._screen)
        self._fruit = Fruit(self._screen)
        self._player = Player(self._screen)

    def user_input(self):
        self._player.user_input()

    def update(self):
        self._grid.update()
        self._player.update()

    def render(self):
        self._screen.fill(c.WHITE)
        self._grid.render()
        self._player.render()
