from src.other.sceneManager import SceneManager
from src.menu.playButton import PlayButton
from src.menu.controlsButton import ControlsButton
import src.other.constants as c


class MenuScene(SceneManager):

    def __init__(self, screen):
        super().__init__(screen)
        self._scene_index = c.MENU_SCENE_INDEX
        self._buttons = self.initialise_buttons()

    def initialise_buttons(self):
        buttons = [PlayButton(self._screen), ControlsButton(self._screen)]
        return buttons

    def user_input(self):
        for button in self._buttons:
            button.user_input()

    def update(self):
        for button in self._buttons:
            button.update()

    def render(self):
        self._screen.fill(c.WHITE)
        for button in self._buttons:
            button.render()

    def change_scene(self):
        for button in self._buttons:
            if button.change_scene() != self._scene_index:
                return button.change_scene()

        return self._scene_index
