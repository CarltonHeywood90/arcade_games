import sys
import pygame
from .logic import PongLogic
from .gui import PongGUI
from .scoreboard import Scoreboard

def main():
    pygame.init()
    
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arcade Hub - Pong")
    
    clock = pygame.time.Clock()
    
    logic = PongLogic(WIDTH, HEIGHT)
    gui = PongGUI(screen)
    scoreboard = Scoreboard()
    
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Continuous keyboard polling for smooth movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
            
        # Left Player (W / S keys)
        if keys[pygame.K_w]:
            logic.move_paddle('left', -1)
        if keys[pygame.K_s]:
            logic.move_paddle('left', 1)
            
        # Right Player (Up / Down arrows)
        if keys[pygame.K_UP]:
            logic.move_paddle('right', -1)
        if keys[pygame.K_DOWN]:
            logic.move_paddle('right', 1)

        # Update game state & physics
        logic.update(scoreboard)
        
        # Render graphics
        gui.draw(logic, scoreboard)
        
        # Lock to 60 FPS
        clock.tick(60)

    return

if __name__ == "__main__":
    main()