print('\n') 

import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite):
    """A Class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object the the shiip's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0 , 0) and then set correct position 
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop 

        # Store the bullet's position as a float 
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        #Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position 
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen with a shadow."""
        shadow_rect = self.rect.copy()
        shadow_rect.x += 2  # shift right for shadow
        shadow_rect.y += 2  # shift down for shadow
        pygame.draw.rect(self.screen, self.color, self.rect)

    