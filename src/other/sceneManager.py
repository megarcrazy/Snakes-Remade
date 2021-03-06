import pygame
from src.other.gameObject import GameObject
from src.other.userInput import UserInput
import src.other.constants as c


class SceneManager(GameObject):

    def __init__(self, screen):
        super().__init__(screen)
        self._scene_index = None

    def change_scene(self):
        return self._scene_index

    # Pressing the escape key returns the user back to the main menu
    def _return_to_menu(self):
        keys = UserInput.get_keyboard()
        if keys[pygame.K_ESCAPE]:
            self._scene_index = c.MENU_SCENE_INDEX
