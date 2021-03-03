import pygame


class UserInput:

    @staticmethod
    def get_mouse_position():
        return pygame.mouse.get_pos()

    @staticmethod
    def get_mouse_click():
        return pygame.mouse.get_pressed(3)

    @staticmethod
    def get_keyboard():
        return pygame.key.get_pressed()
