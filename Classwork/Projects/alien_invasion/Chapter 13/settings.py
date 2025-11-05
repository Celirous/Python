print('\n') 

import os
import pygame 

class Settings: 
    """A class to store all my settings for the Alien Invasion Game """

    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings 
        self.screen_width = 1200
        self.screen_height = 800

        current_dir = os.path.dirname(__file__)
        background_path = os.path.join(current_dir, 'data', 'pixel_background_invasion.jpg')

        self.background = pygame.image.load(background_path)
        self.background = pygame.transform.scale(self.background, (1200,800))

        #Ship settings:
        self.ship_speed = 3.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        self.bullets_allowed = 8

        #Alien settings 
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20
        # fleet_directions of 1 represent right, -1 represents left
        self.fleet_direction = 1


