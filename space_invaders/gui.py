import pygame

class SpaceInvadersGUI:
    def __init__(self, surface):
        self.surface = surface
        self.bg_color = (10, 10, 20)
        self.player_color = (0, 255, 200)
        self.alien_color = (255, 50, 100)
        self.bullet_color = (255, 255, 100)
        self.alien_bullet_color = (255, 100, 50)
        try:
            self.overlay_font = pygame.font.Font(None, 48)
        except pygame.error:
            self.overlay_font = pygame.font.SysFont("arial", 48)

    def draw(self, logic, scoreboard):
        self.surface.fill(self.bg_color)
        
        # Draw player ship
        pygame.draw.rect(self.surface, self.player_color, logic.player, border_radius=3)
        pygame.draw.rect(self.surface, self.player_color, (logic.player.centerx - 4, logic.player.top - 8, 8, 8))
        
        # Draw aliens from rect dicts
        for alien in logic.aliens:
            r = alien['rect']
            pygame.draw.rect(self.surface, self.alien_color, r, border_radius=4)
            pygame.draw.rect(self.surface, (255, 255, 255), (r.x + 8, r.y + 6, 4, 4))
            pygame.draw.rect(self.surface, (255, 255, 255), (r.right - 12, r.y + 6, 4, 4))
            
        # Draw bullets
        for b in logic.bullets:
            pygame.draw.rect(self.surface, self.bullet_color, b['rect'])
        for ab in logic.alien_bullets:
            pygame.draw.rect(self.surface, self.alien_bullet_color, ab['rect'])
            
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