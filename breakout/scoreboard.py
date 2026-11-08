import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.lives = 3
        try:
            self.font = pygame.font.Font(None, 32)
        except pygame.error:
            self.font = pygame.font.SysFont("arial", 32)

    def draw(self, surface):
        """Renders score and lives text."""
        score_surf = self.font.render(f"SCORE: {self.score}", True, (255, 255, 255))
        lives_surf = self.font.render(f"LIVES: {self.lives}", True, (50, 220, 100))
        surface.blit(score_surf, (30, 20))
        surface.blit(lives_surf, (surface.get_width() - 140, 20))