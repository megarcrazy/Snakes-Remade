import pygame
from src.userInput import UserInput
from src.sceneManager import SceneManager
from src.play.gameLogic import GameLogic
import src.constants as c


class PlayScene(SceneManager):

    def __init__(self, screen):
        super().__init__(screen)
        self._scene_index = c.PLAY_SCENE_INDEX
        self._grid = GameLogic(self._screen)

    def user_input(self):
        self._return_to_menu()
        self._grid.user_input()

    def update(self):
        self._grid.update()

    def render(self):
        self._screen.fill(c.WHITE)
        self._grid.render()
