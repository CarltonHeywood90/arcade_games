import pygame

class PongLogic:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        # Paddle dimensions
        self.paddle_width = 15
        self.paddle_height = 90
        
        # Paddle positions (Left player, Right player)
        self.left_paddle = pygame.Rect(30, (height - self.paddle_height) // 2, self.paddle_width, self.paddle_height)
        self.right_paddle = pygame.Rect(width - 45, (height - self.paddle_height) // 2, self.paddle_width, self.paddle_height)
        
        # Ball configuration
        self.ball_size = 15
        self.ball = pygame.Rect(width // 2 - self.ball_size // 2, height // 2 - self.ball_size // 2, self.ball_size, self.ball_size)
        self.ball_dx = 22 * (1 if pygame.time.get_ticks() % 2 == 0 else -1)
        self.ball_dy = 12 * (1 if pygame.time.get_ticks() % 3 == 0 else -1)
        
        # Paddle speeds
        self.paddle_speed = 20

    def move_paddle(self, paddle_key, direction):
        """Moves left or right paddle within screen bounds."""
        paddle = self.left_paddle if paddle_key == 'left' else self.right_paddle
        paddle.y += direction * self.paddle_speed
        
        # Keep inside window bounds
        if paddle.top < 0:
            paddle.top = 0
        if paddle.bottom > self.height:
            paddle.bottom = self.height

    def update(self, scoreboard):
        """Updates ball position, handles wall/paddle collisions, and scoring."""
        self.ball.x += self.ball_dx
        self.ball.y += self.ball_dy

        # Bounce off top and bottom walls
        if self.ball.top <= 0 or self.ball.bottom >= self.height:
            self.ball_dy *= -1

        # Bounce off paddles
        if self.ball.colliderect(self.left_paddle) or self.ball.colliderect(self.right_paddle):
            self.ball_dx *= -1
            # Slight speed increase or angle variation on hit could go here

        # Scoring checks (Left wall vs Right wall)
        if self.ball.left <= 0:
            scoreboard.right_score += 1
            self.reset_ball()
        elif self.ball.right >= self.width:
            scoreboard.left_score += 1
            self.reset_ball()

    def reset_ball(self):
        """Resets ball to center and reverses initial direction."""
        self.ball.x = self.width // 2 - self.ball_size // 2
        self.ball.y = self.height // 2 - self.ball_size // 2
        self.ball_dx *= -1