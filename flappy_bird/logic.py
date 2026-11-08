import random
import pygame

class FlappyLogic:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        # Bird setup
        self.bird_x = 100
        self.bird_y = height // 2
        self.bird_size = 30
        self.bird_velocity = 0
        self.gravity = 0.5
        self.jump_strength = -8
        
        # Pipes setup
        self.pipe_width = 70
        self.pipe_gap = 160
        self.pipe_speed = 3
        self.pipes = []
        self.spawn_timer = 0
        
        self.game_over = False

    def jump(self):
        """Applies upward impulse."""
        if self.game_over:
            return
        self.bird_velocity = self.jump_strength

    def update(self, scoreboard):
        """Updates physics, spawns pipes, and checks collisions."""
        if self.game_over:
            return

        # Apply gravity
        self.bird_velocity += self.gravity
        self.bird_y += self.bird_velocity

        # Bird rect for collision checks
        bird_rect = pygame.Rect(self.bird_x, int(self.bird_y), self.bird_size, self.bird_size)

        # Ceiling collision / floor collision
        if bird_rect.top <= 0:
            bird_rect.top = 0
            self.bird_y = 0
            self.bird_velocity = 0
        if bird_rect.bottom >= self.height - 50: # Ground line
            self.game_over = True
            return

        # Procedural pipe generation
        self.spawn_timer += 1
        if self.spawn_timer >= 90: # Every 1.5 seconds at 60 FPS
            self.spawn_timer = 0
            min_height = 80
            max_height = self.height - self.pipe_gap - 120
            top_height = random.randint(min_height, max_height)
            
            top_pipe = pygame.Rect(self.width, 0, self.pipe_width, top_height)
            bottom_pipe = pygame.Rect(self.width, top_height + self.pipe_gap, self.pipe_width, self.height - (top_height + self.pipe_gap))
            self.pipes.append({'top': top_pipe, 'bottom': bottom_pipe, 'passed': False})

        # Update pipes
        for pipe in self.pipes[:]:
            pipe['top'].x -= self.pipe_speed
            pipe['bottom'].x -= self.pipe_speed

            # Remove off-screen pipes
            if pipe['top'].right < 0:
                self.pipes.remove(pipe)
                continue

            # Check if bird passed pipe for scoring
            if not pipe['passed'] and pipe['top'].right < self.bird_x:
                scoreboard.score += 1
                pipe['passed'] = True

            # Check collision with bird
            if bird_rect.colliderect(pipe['top']) or bird_rect.colliderect(pipe['bottom']):
                self.game_over = True