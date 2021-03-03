import pygame
from src.gameObject import GameObject
from src.user_input import UserInput
import src.constants as c


class Button(GameObject):

    def __init__(self, screen, rect, text=""):
        super().__init__(screen)
        self._rect = self._center_rectangle(rect)

        self._font = pygame.font.SysFont('Comic Sans MS', 30)
        self._text = self._font.render(text, False, (0, 0, 0))

        self._center = rect[:2]
        self._hover = False
        self._clicked = False

        self._scene_index_pointer = None

    def user_input(self):
        self._mouse_position = UserInput.get_mouse_position()
        self._mouse_click = UserInput.get_mouse_click()

    def update(self):
        self.is_hover(self._mouse_position)
        self.is_clicked(self._mouse_click)

    def render(self):
        self._render_button_background()
        self._render_button_text()

    def change_scene(self):
        return self._scene_index_pointer

    def _render_button_background(self):
        button_colour = c.BUTTON_COLOUR
        if self._hover:
            button_colour = c.HOVER_BUTTON_COLOUR
        pygame.draw.rect(self._screen, button_colour, self._rect)

    def _render_button_text(self):
        text_rect = self._text.get_rect(center=self._center)
        self._screen.blit(self._text, text_rect)

    @staticmethod
    def _center_rectangle(rect):
        x, y, width, height = rect
        center_rect = [
            x - width // 2,
            y - height // 2,
            width,
            height
        ]
        return center_rect

    def is_hover(self, mouse_position):
        x1, y1, x2, y2 = [
            self._rect[0], self._rect[1],
            self._rect[0] + self._rect[2], self._rect[1] + self._rect[3]
        ]
        self._hover = x1 < mouse_position[0] < x2 and y1 < mouse_position[1] < y2

    def is_clicked(self, mouse_click):
        if self._hover:
            if mouse_click[0]:
                self._clicked = True
            elif self._clicked:
                if not mouse_click[0]:
                    self.get_scene_pointer()
        else:
            self._clicked = False

    def get_scene_pointer(self):
        pass
