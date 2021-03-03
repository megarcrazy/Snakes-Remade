class GameObject:

    def __init__(self, screen):
        self._screen = screen
        self._mouse_position = None
        self._mouse_click = None
        self._keyboard = None

    def user_input(self):
        pass

    def update(self):
        pass

    def render(self):
        pass
