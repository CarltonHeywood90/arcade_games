import pygame

class PongGUI:
    def __init__(self, surface):
        self.surface = surface
        self.bg_color = (20, 20, 30)
        self.paddle_color = (255, 255, 255)
        self.ball_color = (255, 200, 50)
        self.line_color = (60, 60, 80)

    def draw(self, logic, scoreboard):
        """Fills background, draws center net, paddles, ball, and score."""
        self.surface.fill(self.bg_color)
        
        # Draw dashed center line
        for y in range(0, self.surface.get_height(), 30):
            pygame.draw.rect(self.surface, self.line_color, (self.surface.get_width() // 2 - 2, y, 4, 15))
            
        # Draw paddles
        pygame.draw.rect(self.surface, self.paddle_color, logic.left_paddle)
        pygame.draw.rect(self.surface, self.paddle_color, logic.right_paddle)
        
        # Draw ball
        pygame.draw.rect(self.surface, self.ball_color, logic.ball)
        
        # Draw scoreboard
        scoreboard.draw(self.surface, self.surface.get_width())
        
        pygame.display.flip()