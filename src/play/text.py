import pygame
from src.gameObject import GameObject
import src.constants as c


class Text(GameObject):

    def __init__(self, screen):
        super().__init__(screen)
        self._font = pygame.font.SysFont('Comic Sans MS', 30)
        self._text = self._font.render("You Lose", False, c.BLACK)

    def render(self):
        text_rect = self._text.get_rect(center=(c.SCREEN_WIDTH//2, c.SCREEN_HEIGHT//2))
        self._screen.blit(self._text, text_rect)
