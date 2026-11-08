import random
import pygame

class SpaceInvadersLogic:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        # Player setup
        self.player = pygame.Rect(width // 2 - 25, height - 60, 50, 25)
        self.player_speed = 12
        
        # Bullets
        self.bullets = []
        self.alien_bullets = []
        
        # Aliens grid setup (5 rows, 10 columns)
        self.alien_rows = 5
        self.alien_cols = 10
        self.aliens = []
        self.alien_dx = 4
        self.alien_drop = 15
        
        self.init_aliens()
        
        self.game_over = False
        self.victory = False

    def init_aliens(self):
        """Populates the alien grid with rects and tracked row indices."""
        self.aliens = []
        alien_width, alien_height = 36, 24
        padding_x, padding_y = 15, 12
        start_x = (self.width - (self.alien_cols * (alien_width + padding_x))) // 2
        start_y = 60

        for row in range(self.alien_rows):
            for col in range(self.alien_cols):
                x = start_x + col * (alien_width + padding_x)
                y = start_y + row * (alien_height + padding_y)
                rect = pygame.Rect(x, y, alien_width, alien_height)
                # Store dict with rect and stable row index
                self.aliens.append({'rect': rect, 'row': row})

    def move_player(self, direction):
        if self.game_over or self.victory:
            return
        self.player.x += direction * self.player_speed
        if self.player.left < 10:
            self.player.left = 10
        if self.player.right > self.width - 10:
            self.player.right = self.width - 10

    def shoot(self):
        if self.game_over or self.victory:
            return
        if len([b for b in self.bullets if b['type'] == 'player']) < 3:
            bullet_rect = pygame.Rect(self.player.centerx - 2, self.player.top - 12, 4, 12)
            self.bullets.append({'rect': bullet_rect, 'type': 'player', 'speed': -10})

    def update(self, scoreboard):
        if self.game_over or self.victory:
            return

        # 1. Update player bullets
        for bullet in self.bullets[:]:
            bullet['rect'].y += bullet['speed']
            if bullet['rect'].bottom < 0:
                self.bullets.remove(bullet)
                continue

            # Check collision with aliens
            hit_alien = None
            for alien in self.aliens:
                if bullet['rect'].colliderect(alien['rect']):
                    hit_alien = alien
                    break
            if hit_alien:
                self.aliens.remove(hit_alien)
                self.bullets.remove(bullet)
                
                # FIXED SCORING: Using stable row index (Row 0 = top/500 pts, Row 4 = bottom/100 pts)
                scoreboard.score += 100 * (self.alien_rows - hit_alien['row'])
                
                if not self.aliens:
                    self.victory = True
                continue

        # 2. Update alien grid movement & wall bounces
        edge_hit = False
        for alien in self.aliens:
            alien['rect'].x += self.alien_dx
            if alien['rect'].right >= self.width - 20 or alien['rect'].left <= 20:
                edge_hit = True

        if edge_hit:
            self.alien_dx *= -1
            for alien in self.aliens:
                alien['rect'].y += self.alien_drop
                if alien['rect'].bottom >= self.player.top:
                    self.game_over = True

        # 3. Random alien shooting
        if self.aliens and random.random() < 0.03:
            shooter = random.choice(self.aliens)
            ab_rect = pygame.Rect(shooter['rect'].centerx - 2, shooter['rect'].bottom, 4, 12)
            self.alien_bullets.append({'rect': ab_rect, 'type': 'alien', 'speed': 5})

        # 4. Update alien bullets
        for ab in self.alien_bullets[:]:
            ab['rect'].y += ab['speed']
            if ab['rect'].top > self.height:
                self.alien_bullets.remove(ab)
                continue

            if ab['rect'].colliderect(self.player):
                self.alien_bullets.remove(ab)
                scoreboard.lives -= 1
                if scoreboard.lives <= 0:
                    self.game_over = True
                else:
                    self.player.x = self.width // 2 - 25