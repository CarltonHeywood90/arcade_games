import pygame

class SnakeGUI:
    def __init__(self, surface, block_size=20):
        self.surface = surface
        self.block_size = block_size
        self.bg_color = (15, 15, 25)
        self.snake_head_color = (50, 220, 100)
        self.snake_body_color = (30, 160, 70)
        self.food_color = (255, 60, 60)
        try:
            self.game_over_font = pygame.font.Font(None, 48)
        except pygame.error:
            self.game_over_font = pygame.font.SysFont("arial", 48)

    def draw(self, logic, scoreboard):
        """Clears screen and renders game entities."""
        self.surface.fill(self.bg_color)
        
        # Draw food
        fx, fy = logic.food
        food_rect = pygame.Rect(fx * self.block_size, fy * self.block_size, self.block_size - 2, self.block_size - 2)
        pygame.draw.rect(self.surface, self.food_color, food_rect, border_radius=4)
        
        # Draw snake body
        for i, segment in enumerate(logic.snake):
            sx, sy = segment
            seg_rect = pygame.Rect(sx * self.block_size, sy * self.block_size, self.block_size - 2, self.block_size - 2)
            color = self.snake_head_color if i == 0 else self.snake_body_color
            pygame.draw.rect(self.surface, color, seg_rect, border_radius=4)
            
        # Draw scoreboard
        scoreboard.draw(self.surface)
        
        # Draw Game Over overlay
        if logic.game_over:
            overlay = pygame.Surface((self.surface.get_width(), self.surface.get_height()), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            self.surface.blit(overlay, (0, 0))
            
            go_surf = self.game_over_font.render("GAME OVER - Press R to Restart", True, (255, 255, 255))
            go_rect = go_surf.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2))
            self.surface.blit(go_surf, go_rect)
            
        pygame.display.flip()