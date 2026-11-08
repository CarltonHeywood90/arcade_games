import pygame

class Scoreboard:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0
        try:
            self.font = pygame.font.Font(None, 64)
        except pygame.error:
            self.font = pygame.font.SysFont("arial", 64)

    def draw(self, surface, width):
        """Draws the current scores centered at the top of the screen."""
        score_text = f"{self.left_score}   {self.right_score}"
        text_surface = self.font.render(score_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width // 2, 40))
        surface.blit(text_surface, text_rect)