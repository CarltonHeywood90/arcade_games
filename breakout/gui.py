import pygame

class BreakoutGUI:
    def __init__(self, surface):
        self.surface = surface
        self.bg_color = (15, 15, 25)
        self.border_color = (60, 60, 90)
        self.paddle_color = (255, 255, 255)
        self.ball_color = (255, 220, 50)
        try:
            self.overlay_font = pygame.font.Font(None, 48)
        except pygame.error:
            self.overlay_font = pygame.font.SysFont("arial", 48)

    def draw(self, logic, scoreboard):
        self.surface.fill(self.bg_color)
        
        # Draw arcade side/top borders
        pygame.draw.rect(self.surface, self.border_color, (0, 0, self.surface.get_width(), 15))
        pygame.draw.rect(self.surface, self.border_color, (0, 0, 15, self.surface.get_height()))
        pygame.draw.rect(self.surface, self.border_color, (self.surface.get_width() - 15, 0, 15, self.surface.get_height()))
        
        # Draw bricks
        for brick in logic.bricks:
            r = brick['rect']
            pygame.draw.rect(self.surface, brick['color'], r, border_radius=3)
            # Subtle highlight on brick
            pygame.draw.line(self.surface, (255, 255, 255), (r.x + 3, r.y + 3), (r.right - 3, r.y + 3), 2)
            
        # Draw paddle
        pygame.draw.rect(self.surface, self.paddle_color, logic.paddle, border_radius=4)
        
        # Draw ball
        pygame.draw.rect(self.surface, self.ball_color, logic.ball, border_radius=3)
        
        # Draw scoreboard
        scoreboard.draw(self.surface)
        
        # Game Over / Victory Overlay
        if logic.game_over or logic.victory:
            overlay = pygame.Surface((self.surface.get_width(), self.surface.get_height()), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self.surface.blit(overlay, (0, 0))
            
            msg = "VICTORY! Press R to Restart" if logic.victory else "GAME OVER - Press R to Restart"
            color = (50, 255, 100) if logic.victory else (255, 50, 50)
            
            msg_surf = self.overlay_font.render(msg, True, color)
            msg_rect = msg_surf.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2))
            self.surface.blit(msg_surf, msg_rect)
            
        pygame.display.flip()