from src.menu.button import Button
import src.constants as c


class PlayButton(Button):

    def __init__(self, screen):
        rect = [c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 3, 300, 100]
        super().__init__(screen, rect=rect, text="Play")
        self._scene_index_pointer = c.MENU_SCENE_INDEX

    def get_scene_pointer(self):
        self._scene_index_pointer = c.PLAY_SCENE_INDEX
