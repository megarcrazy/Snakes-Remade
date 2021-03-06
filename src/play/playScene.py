from src.other.sceneManager import SceneManager
from src.play.gameLogic import GameLogic
import src.other.constants as c


class PlayScene(SceneManager):

    def __init__(self, screen):
        super().__init__(screen)
        self._scene_index = c.PLAY_SCENE_INDEX
        self._logic = GameLogic(self._screen)

    def user_input(self):
        self._return_to_menu()
        self._logic.user_input()

    def update(self):
        self._logic.update()

    def render(self):
        self._screen.fill(c.WHITE)
        self._logic.render()
