from src.gameObject import GameObject


class Grid(GameObject):

    def __init__(self, screen):
        super().__init__(screen)
        self._screen = screen

    def update(self):
        pass

    def render(self):
        pass
