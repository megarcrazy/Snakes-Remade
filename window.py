import pygame
import constants as c


class Window:

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

    def run(self):
        state = True
        while state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = False

            self.update()

            pygame.display.flip()
            pygame.time.delay(1)

    def update(self):
        self._screen.fill((255, 255, 255))
