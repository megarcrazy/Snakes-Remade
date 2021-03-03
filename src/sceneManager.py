from src.gameObject import GameObject
from src.user_input import UserInput


class SceneManager(GameObject):

    def __init__(self, screen):
        super().__init__(screen)
        self._scene_index = None

    def change_scene(self):
        return self._scene_index
