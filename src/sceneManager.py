import pygame
from src.gameObject import GameObject
from src.userInput import UserInput
import src.constants as c


class SceneManager(GameObject):

    def __init__(self, screen):
        super().__init__(screen)
        self._scene_index = None

    def change_scene(self):
        return self._scene_index

    def _return_to_menu(self):
        keys = UserInput.get_keyboard()
        if keys[pygame.K_ESCAPE]:
            self._scene_index = c.MENU_SCENE_INDEX