class GameObject:

    def __init__(self, screen):
        self._screen = screen

        # User inputs
        self._mouse_position = None
        self._mouse_click = None
        self._keyboard = None

    # Takes the required key and mouse inputs using the Pygame module
    def user_input(self):
        pass

    # Update the game object for each call
    def update(self):
        pass

    # Draws graphics on the Pygame window
    def render(self):
        pass
