import random
import pygame

class SnakeLogic:
    def __init__(self, width, height, block_size=20):
        self.width = width
        self.height = height
        self.block_size = block_size
        
        # Grid dimensions
        self.cols = width // block_size
        self.rows = height // block_size
        
        # Initialize snake in the center (list of [x, y] coordinates)
        start_x = self.cols // 2
        start_y = self.rows // 2
        self.snake = [
            [start_x, start_y],
            [start_x - 1, start_y],
            [start_x - 2, start_y]
        ]
        
        # Initial direction (dx, dy): moving right
        self.dx = 1
        self.dy = 0
        self.next_dx = 1
        self.next_dy = 0
        
        # Food position
        self.food = self.spawn_food()
        self.game_over = False

    def spawn_food(self):
        """Spawns food at a random grid coordinate not occupied by the snake."""
        while True:
            fx = random.randint(0, self.cols - 1)
            fy = random.randint(0, self.rows - 1)
            if [fx, fy] not in self.snake:
                return [fx, fy]

    def change_direction(self, new_dx, new_dy):
        """Prevents instant 180-degree reversals into oneself."""
        if (new_dx != -self.dx or new_dy != -self.dy):
            self.next_dx = new_dx
            self.next_dy = new_dy

    def update(self, scoreboard):
        """Advances the snake, checks collisions, and handles eating food."""
        if self.game_over:
            return

        # Lock in directional input for this tick
        self.dx = self.next_dx
        self.dy = self.next_dy

        # Calculate new head position
        head_x, head_y = self.snake[0]
        new_head = [head_x + self.dx, head_y + self.dy]

        # Check wall collisions
        if new_head[0] < 0 or new_head[0] >= self.cols or new_head[1] < 0 or new_head[1] >= self.rows:
            self.game_over = True
            return

        # Check self-collision
        if new_head in self.snake:
            self.game_over = True
            return

        # Insert new head
        self.snake.insert(0, new_head)

        # Check if food is eaten
        if new_head == self.food:
            scoreboard.score += 10
            self.food = self.spawn_food()
        else:
            # Pop tail if no food eaten to maintain length
            self.snake.pop()