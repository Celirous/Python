print('\n') 

import os 
import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set the group"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load The alien image and set its rect attirubute 
        current_dir = os.path.dirname(__file__) 
        alien_path = os.path.join(current_dir, 'data', 'alien_ships_red.png')
        self.image = pygame.image.load(alien_path)
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen. 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store Alien's exact horizontal position 
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction 
        self.rect.x = self.x 



    
