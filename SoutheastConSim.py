import pygame
from RealWorldInfo import *


class SoutheastConSim:
    def __init__(self, width_p=700, height_p=700, headless=False, players=None):
        """
        Virtual representation of Southeast Con 2019 playing field.
        """
        # todo: handle player creation

        self.real_world_converter = RealWorldInfo(width_p, height_p)

        self.headless = headless
        if not self.headless:
            pygame.init()
            self.screen = pygame.display.set_mode((width_p, height_p))
            pygame.display.set_caption("Southeastcon 2019 Simulator")
            self.clock = pygame.time.Clock()

    def inputUpdate(self):
        input_events = pygame.event.get()

        for event in input_events:
            if event.type == pygame.QUIT:
                return False

        return True

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(0, 0, 100, 100))
        pygame.display.flip()

    def run(self):
        running = True

        while running:
            if not self.headless:
                self.draw()

            running = self.inputUpdate()
            self.clock.tick(60)

        pygame.quit()
        exit()

if __name__ == "__main__":
    sec19 = SoutheastConSim()
    sec19.run()
