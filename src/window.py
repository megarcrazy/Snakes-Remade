import pygame
from src.menu.menuScene import MenuScene
from src.play.playScene import PlayScene
from src.controls.controlsScene import ControlsScene
import src.constants as c


class Window:

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pygame.display.set_caption(c.TITLE)
        self._current_scene_index = c.MENU_SCENE_INDEX
        self._scene = MenuScene(self._screen)

        self._tick_counter = 0

    def run(self):
        state = True
        while state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = False

            self._scene.user_input()
            if self._tick_counter == c.PYGAME_DELAY//c.INPUT_DELAY:
                self._scene.update()
                self._scene.render()
                self._tick_counter = 0
                self.change_scene(self._scene.change_scene())

            pygame.display.flip()
            pygame.time.delay(c.INPUT_DELAY)
            self._tick_counter += 1

    def change_scene(self, scene_index):
        if scene_index != self._current_scene_index:
            if scene_index == c.MENU_SCENE_INDEX:
                self._scene = MenuScene(self._screen)
            elif scene_index == c.PLAY_SCENE_INDEX:
                self._scene = PlayScene(self._screen)
            elif scene_index == c.CONTROLS_SCENE_INDEX:
                self._scene = ControlsScene(self._screen)

        self._current_scene_index = scene_index
