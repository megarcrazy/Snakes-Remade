import pygame
from src.user_input import UserInput
from src.sceneManager import SceneManager
from src.play.grid import Grid
import src.constants as c


class Play(SceneManager):

    def __init__(self, screen):
        super().__init__(screen)
        self._scene_index = c.PLAY_SCENE_INDEX
        self._grid = Grid(self._screen)

    def user_input(self):
        self._return_to_menu()
        self._grid.user_input()

    def update(self):
        self._grid.update()

    def render(self):
        self._screen.fill(c.WHITE)
        self._grid.render()

    def _return_to_menu(self):
        keys = UserInput.get_keyboard()
        if keys[pygame.K_ESCAPE]:
            self._scene_index = c.MENU_SCENE_INDEX
