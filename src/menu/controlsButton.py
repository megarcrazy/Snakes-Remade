from src.menu.button import Button
import src.constants as c


class ControlsButton(Button):

    def __init__(self, screen):
        rect = [c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT * 2 // 3, 300, 100]
        super().__init__(screen, rect=rect, text="Controls")
        self._scene_index_pointer = c.MENU_SCENE_INDEX

    def get_scene_pointer(self):
        self._scene_index_pointer = c.CONTROLS_SCENE_INDEX
