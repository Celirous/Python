print('\n') 

import os
import pygame

class Ship: 
    """A class to manage the ship. """
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the shop image 
        current_dir = os.path.dirname(__file__) 
        ship_path = os.path.join(current_dir, 'data', 'yellow_ship.png') 
        self.image = pygame.image.load(ship_path)
        self.image = pygame.transform.scale(self.image, (64, 80))
        self.rect = self.image.get_rect()


        #Start each new ship at the bottom centre of the screen. 
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position 
        self.x = float(self.rect.x)

        # Movement flags; start with a ship that is not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the moment flag"""
        #Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right: # In english this says, if ship movement and ship location is smaller than the screen size, let it go, if it is bigger than screen size, kill code
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Update rect object from self.x 
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)