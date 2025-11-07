print('\n') 

# ======================== Start of project, chapter 12

import os
import sys
from time import sleep

import pygame 

from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))#, pygame.FULLSCREEN)
        pygame.display.set_caption("Alien Invasion")

        #Create an instance to store game stats and create a scoreboard 
        #create an instant to store game stats
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Make the Play button. 
        self.play_button = Button(self, "Play")

        

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                # print(len(self.bullets)) # number of bullets on the screen
                self._update_aliens()
                
            self._update_screen()
            self.clock.tick(60)

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            #Decrese ships left, and update scoreboard
            self.stats.ships_left -= 1 
            self.sb.prep_ship()


            #Get rid of any remaining bullets and aliens. 
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship. 
            self._create_fleet()
            self.ship.center_ship()

            #Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)



    def _check_events(self):
        """Respond to keypressed and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings:
            self.settings.initialize_dynamic_settings()
            # Reset the game stats
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()  
            self.sb.prep_ship()

            self.game_active = True
            #Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            #Create new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

            #Hide the mouse cursor.
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key realeases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets"""
        # Update bullet Positions. 
        self.bullets.update()

        # Get rid of bullets that have dissapeared. 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collision"""
        # Remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            # self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            self.sb.check_high_score()

              
        if not self.aliens:
            #Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.inscrease_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        """Updates images on the screen, and flip to the new screen"""
        self.screen.blit(self.settings.background, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the score info
        self.sb.show_score()

        # Draw the play button if the game is inactive. 
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        #Make an alien.
        #Create an aline and keep adding untill there is no room left 
        #Spacing between aliens is one alien width and one alein height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 6 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            #Finish a row, reset x value, increment y value
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions"""
        self._check_fleet_edges()
        self.aliens.update()

        #Look for alien-ship collisions. 
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens ave reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop entire fleet and change fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the ottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #Treat this the same if if the ship got hit
                self._ship_hit()
                break

if __name__ == '__main__':
    # Make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()


