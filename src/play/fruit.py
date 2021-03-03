from src.gameObject import GameObject


class Fruit(GameObject):

    def __init__(self, screen):
        super().__init__(screen)
        self._screen = screen
