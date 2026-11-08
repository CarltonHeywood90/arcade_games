import sys
import pygame

# Import main functions from each game subfolder
from pong.main import main as run_pong
from snake.main import main as run_snake
from space_invaders.main import main as run_space_invaders
from breakout.main import main as run_breakout
from flappy_bird.main import main as run_flappy

class ArcadeMenu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        
        self.games = [
            {"title": "1. PONG", "runner": run_pong, "color": (50, 200, 255)},
            {"title": "2. SNAKE", "runner": run_snake, "color": (50, 220, 100)},
            {"title": "3. SPACE INVADERS", "runner": run_space_invaders, "color": (255, 50, 100)},
            {"title": "4. BREAKOUT", "runner": run_breakout, "color": (255, 200, 50)},
            {"title": "5. FLAPPY BIRD", "runner": run_flappy, "color": (200, 100, 255)},
        ]
        
        self.selected_index = 0
        
        try:
            self.title_font = pygame.font.Font(None, 64)
            self.menu_font = pygame.font.Font(None, 40)
            self.hint_font = pygame.font.Font(None, 24)
        except pygame.error:
            self.title_font = pygame.font.SysFont("arial", 64)
            self.menu_font = pygame.font.SysFont("arial", 40)
            self.hint_font = pygame.font.SysFont("arial", 24)

    def draw(self):
        self.screen.fill((15, 15, 30))
        
        # Header Title
        title_surf = self.title_font.render("PYTHON ARCADE HUB", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(self.width // 2, 70))
        self.screen.blit(title_surf, title_rect)
        
        # Subtitle / Instructions
        hint_surf = self.hint_font.render("Use UP/DOWN Arrows & ENTER to Select | Press ESC to Exit Game", True, (150, 150, 180))
        hint_rect = hint_surf.get_rect(center=(self.width // 2, 120))
        self.screen.blit(hint_surf, hint_rect)

        # Menu List
        start_y = 180
        spacing = 55
        for i, game in enumerate(self.games):
            is_selected = (i == self.selected_index)
            prefix = "> " if is_selected else "  "
            color = game["color"] if is_selected else (120, 120, 140)
            
            text_surf = self.menu_font.render(f"{prefix}{game['title']}", True, color)
            text_rect = text_surf.get_rect(center=(self.width // 2, start_y + i * spacing))
            
            # Selection Highlight Box
            if is_selected:
                bg_rect = text_rect.inflate(40, 10)
                pygame.draw.rect(self.screen, (30, 30, 50), bg_rect, border_radius=6)
                pygame.draw.rect(self.screen, color, bg_rect, width=2, border_radius=6)
                
            self.screen.blit(text_surf, text_rect)

        pygame.display.flip()

    def run_selected_game(self):
        """Launches the selected game and resizes the menu screen upon return."""
        game_runner = self.games[self.selected_index]["runner"]
        
        # Launch game loop
        game_runner()
        
        # Re-initialize main display once returning to launcher
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Python Arcade Hub")


def main():
    pygame.init()
    
    WIDTH, HEIGHT = 700, 550
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Python Arcade Hub")
    
    clock = pygame.time.Clock()
    menu = ArcadeMenu(screen, WIDTH, HEIGHT)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    menu.selected_index = (menu.selected_index - 1) % len(menu.games)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    menu.selected_index = (menu.selected_index + 1) % len(menu.games)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    menu.run_selected_game()
                # Direct number selection
                elif event.key in (pygame.K_1, pygame.K_KP1):
                    menu.selected_index = 0
                    menu.run_selected_game()
                elif event.key in (pygame.K_2, pygame.K_KP2):
                    menu.selected_index = 1
                    menu.run_selected_game()
                elif event.key in (pygame.K_3, pygame.K_KP3):
                    menu.selected_index = 2
                    menu.run_selected_game()
                elif event.key in (pygame.K_4, pygame.K_KP4):
                    menu.selected_index = 3
                    menu.run_selected_game()
                elif event.key in (pygame.K_5, pygame.K_KP5):
                    menu.selected_index = 4
                    menu.run_selected_game()

        menu.draw()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()