import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        try:
            self.font = pygame.font.Font(None, 36)
        except pygame.error:
            self.font = pygame.font.SysFont("arial", 36)

    def draw(self, surface):
        """Renders current score."""
        text_surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        surface.blit(text_surface, (20, 20))