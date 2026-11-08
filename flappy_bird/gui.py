import pygame

class FlappyGUI:
    def __init__(self, surface):
        self.surface = surface
        self.bg_color = (70, 130, 180)     # Sky blue
        self.bird_color = (255, 215, 0)    # Gold
        self.pipe_color = (34, 139, 34)    # Forest green
        self.floor_color = (222, 184, 135) # Tan ground
        try:
            self.overlay_font = pygame.font.Font(None, 42)
        except pygame.error:
            self.overlay_font = pygame.font.SysFont("arial", 42)

    def draw(self, logic, scoreboard):
        self.surface.fill(self.bg_color)
        
        # Draw pipes
        for pipe in logic.pipes:
            pygame.draw.rect(self.surface, self.pipe_color, pipe['top'], border_radius=4)
            pygame.draw.rect(self.surface, self.pipe_color, pipe['bottom'], border_radius=4)
            # Pipe cap lips
            pygame.draw.rect(self.surface, (0, 100, 0), (pipe['top'].x - 4, pipe['top'].bottom - 20, 78, 20), border_radius=3)
            pygame.draw.rect(self.surface, (0, 100, 0), (pipe['bottom'].x - 4, pipe['bottom'].y, 78, 20), border_radius=3)

        # Draw ground floor
        floor_rect = pygame.Rect(0, self.surface.get_height() - 50, self.surface.get_width(), 50)
        pygame.draw.rect(self.surface, self.floor_color, floor_rect)
        pygame.draw.line(self.surface, (50, 200, 50), (0, self.surface.get_height() - 50), (self.surface.get_width(), self.surface.get_height() - 50), 6)

        # Draw bird
        bird_rect = pygame.Rect(logic.bird_x, int(logic.bird_y), logic.bird_size, logic.bird_size)
        pygame.draw.rect(self.surface, self.bird_color, bird_rect, border_radius=8)
        # Bird eye and beak detail
        pygame.draw.circle(self.surface, (0, 0, 0), (bird_rect.right - 8, bird_rect.top + 10), 3)
        pygame.draw.polygon(self.surface, (255, 140, 0), [
            (bird_rect.right, bird_rect.top + 10), 
            (bird_rect.right + 10, bird_rect.top + 14), 
            (bird_rect.right, bird_rect.top + 18)
        ])

        # Draw scoreboard
        scoreboard.draw(self.surface)

        # Game Over Overlay
        if logic.game_over:
            overlay = pygame.Surface((self.surface.get_width(), self.surface.get_height()), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self.surface.blit(overlay, (0, 0))
            
            go_surf = self.overlay_font.render("GAME OVER - Press R to Restart", True, (255, 50, 50))
            go_rect = go_surf.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2))
            self.surface.blit(go_surf, go_rect)

        pygame.display.flip()