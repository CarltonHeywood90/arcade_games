import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        try:
            self.font = pygame.font.Font(None, 56)
        except pygame.error:
            self.font = pygame.font.SysFont("arial", 56)

    def draw(self, surface):
        """Renders score centered at the top."""
        score_surf = self.font.render(str(self.score), True, (255, 255, 255))
        score_rect = score_surf.get_rect(center=(surface.get_width() // 2, 60))
        surface.blit(score_surf, score_rect)