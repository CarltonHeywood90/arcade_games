import sys
import pygame
from .logic import SpaceInvadersLogic
from .gui import SpaceInvadersGUI
from .scoreboard import Scoreboard

def main():
    pygame.init()
    
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arcade Hub - Space Invaders")
    
    clock = pygame.time.Clock()
    
    logic = SpaceInvadersLogic(WIDTH, HEIGHT)
    gui = SpaceInvadersGUI(screen)
    scoreboard = Scoreboard()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    logic.shoot()
                elif event.key == pygame.K_r and (logic.game_over or logic.victory):
                    logic = SpaceInvadersLogic(WIDTH, HEIGHT)
                    scoreboard = Scoreboard()

        # Continuous keyboard polling for smooth ship movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            logic.move_player(-1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            logic.move_player(1)

        # Update game physics and collision state
        logic.update(scoreboard)
        
        # Render graphics
        gui.draw(logic, scoreboard)
        
        # Lock to 60 FPS
        clock.tick(60)

    return

if __name__ == "__main__":
    main()