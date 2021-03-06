import pygame
from src.other.gameObject import GameObject
import src.other.constants as c


class CommandLine(GameObject):

    def __init__(self, screen, text, position):
        super().__init__(screen)
        self._font = pygame.font.SysFont('Comic Sans MS', 30)
        self._text = self._font.render(text, False, c.BLACK)
        self._position = position

    def render(self):
        self._screen.blit(self._text, self._position)
