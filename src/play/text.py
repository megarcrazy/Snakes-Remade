import pygame
from src.other.gameObject import GameObject
import src.other.constants as c


class Text(GameObject):

    def __init__(self, screen):
        super().__init__(screen)
        self._font = pygame.font.SysFont('Comic Sans MS', 30)
        self._text = self._font.render("You Lose", False, c.BLACK)

    def render(self):
        # Centre align text in textbox
        centre = c.SCREEN_WIDTH//2, c.SCREEN_HEIGHT//2
        text_rect = self._text.get_rect(center=centre)

        # Draw textbox border
        pygame.draw.rect(self._screen, c.BLACK, text_rect, width=5)

        # Draw textbox background
        pygame.draw.rect(self._screen, c.WHITE, text_rect)

        # Draw text
        self._screen.blit(self._text, text_rect)
