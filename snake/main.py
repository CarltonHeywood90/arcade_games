import sys
import pygame
from .logic import SnakeLogic
from .gui import SnakeGUI
from .scoreboard import Scoreboard

def main():
    pygame.init()
    
    WIDTH, HEIGHT = 600, 600
    BLOCK_SIZE = 20
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arcade Hub - Snake")
    
    clock = pygame.time.Clock()
    
    logic = SnakeLogic(WIDTH, HEIGHT, BLOCK_SIZE)
    gui = SnakeGUI(screen, BLOCK_SIZE)
    scoreboard = Scoreboard()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r and logic.game_over:
                    # Reset game state
                    logic = SnakeLogic(WIDTH, HEIGHT, BLOCK_SIZE)
                    scoreboard = Scoreboard()
                
                # Directional inputs
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    logic.change_direction(0, -1)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    logic.change_direction(0, 1)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    logic.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    logic.change_direction(1, 0)

        # Update game state
        logic.update(scoreboard)
        
        # Render graphics
        gui.draw(logic, scoreboard)
        
        # Control game speed (Snake runs at 10 ticks per second)
        clock.tick(10)

    return

if __name__ == "__main__":
    main()