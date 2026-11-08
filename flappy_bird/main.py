import sys
import pygame
from .logic import FlappyLogic
from .gui import FlappyGUI
from .scoreboard import Scoreboard

def main():
    pygame.init()
    
    WIDTH, HEIGHT = 500, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arcade Hub - Flappy Bird")
    
    clock = pygame.time.Clock()
    
    logic = FlappyLogic(WIDTH, HEIGHT)
    gui = FlappyGUI(screen)
    scoreboard = Scoreboard()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    logic.jump()
                elif event.key == pygame.K_r and logic.game_over:
                    logic = FlappyLogic(WIDTH, HEIGHT)
                    scoreboard = Scoreboard()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if logic.game_over:
                    logic = FlappyLogic(WIDTH, HEIGHT)
                    scoreboard = Scoreboard()
                else:
                    logic.jump()

        # Update game state
        logic.update(scoreboard)
        
        # Render graphics
        gui.draw(logic, scoreboard)
        
        # Lock to 60 FPS
        clock.tick(60)

    return

if __name__ == "__main__":
    main()