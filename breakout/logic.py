import pygame

class BreakoutLogic:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        # Paddle setup
        self.paddle = pygame.Rect(width // 2 - 50, height - 50, 100, 15)
        self.paddle_speed = 5
        
        # Ball setup
        self.ball_size = 12
        self.ball = pygame.Rect(width // 2 - 6, height // 2, self.ball_size, self.ball_size)
        self.ball_dx = 4
        self.ball_dy = -5
        
        # Bricks setup (5 rows, 10 columns)
        self.brick_rows = 5
        self.brick_cols = 10
        self.bricks = []
        self.init_bricks()
        
        self.game_over = False
        self.victory = False

    def init_bricks(self):
        """Generates the grid of breakable bricks with color tiers."""
        self.bricks = []
        brick_width = 70
        brick_height = 20
        padding_x = 8
        padding_y = 8
        start_x = (self.width - (self.brick_cols * (brick_width + padding_x) - padding_x)) // 2
        start_y = 60

        colors = [
            (255, 50, 50),   # Row 0: Red (50 pts)
            (255, 150, 50),  # Row 1: Orange (40 pts)
            (255, 255, 50),  # Row 2: Yellow (30 pts)
            (50, 255, 100),  # Row 3: Green (20 pts)
            (50, 150, 255)   # Row 4: Blue (10 pts)
        ]

        for row in range(self.brick_rows):
            for col in range(self.brick_cols):
                x = start_x + col * (brick_width + padding_x)
                y = start_y + row * (brick_height + padding_y)
                rect = pygame.Rect(x, y, brick_width, brick_height)
                self.bricks.append({'rect': rect, 'color': colors[row], 'points': (5 - row) * 10})

    def move_paddle(self, direction):
        """Moves paddle left (-1) or right (1) within bounds."""
        if self.game_over or self.victory:
            return
        self.paddle.x += direction * self.paddle_speed
        if self.paddle.left < 15:
            self.paddle.left = 15
        if self.paddle.right > self.width - 15:
            self.paddle.right = self.width - 15

    def update(self, scoreboard):
        """Updates ball position, handles wall/paddle/brick collisions and lives."""
        if self.game_over or self.victory:
            return

        # Move ball
        self.ball.x += self.ball_dx
        self.ball.y += self.ball_dy

        # Wall collisions (Left & Right)
        if self.ball.left <= 15:
            self.ball.left = 15
            self.ball_dx *= -1
        elif self.ball.right >= self.width - 15:
            self.ball.right = self.width - 15
            self.ball_dx *= -1

        # Ceiling collision
        if self.ball.top <= 15:
            self.ball.top = 15
            self.ball_dy *= -1

        # Bottom boundary (Lose a life)
        if self.ball.top >= self.height:
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                self.game_over = True
            else:
                self.reset_ball()
            return

        # Paddle collision
        if self.ball.colliderect(self.paddle):
            self.ball.bottom = self.paddle.top
            self.ball_dy *= -1
            
            # Add english/spin based on where it hit the paddle
            offset = (self.ball.centerx - self.paddle.centerx) / (self.paddle.width / 2)
            self.ball_dx = int(offset * 6)
            if self.ball_dx == 0:
                self.ball_dx = 1

        # Brick collisions
        hit_brick = None
        for brick in self.bricks:
            if self.ball.colliderect(brick['rect']):
                hit_brick = brick
                break

        if hit_brick:
            self.bricks.remove(hit_brick)
            scoreboard.score += hit_brick['points']
            
            # Determine bounce axis by checking overlap directions
            # Simple approach: reverse dy, but check if hit was more horizontal
            self.ball_dy *= -1
            
            # Check victory condition
            if not self.bricks:
                self.victory = True

    def reset_ball(self):
        """Resets ball position above paddle after losing a life."""
        self.ball.x = self.paddle.centerx - self.ball_size // 2
        self.ball.y = self.paddle.top - 20
        self.ball_dx = 4 * (1 if pygame.time.get_ticks() % 2 == 0 else -1)
        self.ball_dy = -5