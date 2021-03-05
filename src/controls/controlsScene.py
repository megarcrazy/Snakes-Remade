import pygame
from src.sceneManager import SceneManager
from src.userInput import UserInput
from src.controls.commandLine import CommandLine
import src.constants as c


class ControlsScene(SceneManager):

    def __init__(self, screen):
        super().__init__(screen)
        self._text = []
        self._initialise_text()

    def user_input(self):
        self._return_to_menu()

    def render(self):
        self._screen.fill(c.WHITE)
        for text in self._text:
            text.render()

    def _initialise_text(self):
        self._text = [
            CommandLine(self._screen, "Go Up: W", [10, 0]),
            CommandLine(self._screen, "Go Left: A", [10, 40]),
            CommandLine(self._screen, "Go Down: S", [10, 80]),
            CommandLine(self._screen, "Go Right: D", [10, 120]),
            CommandLine(self._screen, "Back to Menu: Esc ", [10, 160])
        ]
