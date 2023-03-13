import pygame
from random import randint
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from control import Controller
from time import sleep
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self) -> None:
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_fleet()
        self._create_star_sky()

        self.controller = Controller(self)

        # Start game in an inactive state
        self.game_active = False

        # Make the Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.controller._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisisons"""
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions"""
        self._check_alien_edge()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen
        self._check_alien_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ship left
            self.stats.ships_left -= 1

            self.reset_session()

            # Pause
            sleep(0.5)

        else:
            self.game_active = False

            # Show the mouse cursor
            pygame.mouse.set_visible(True)

    def reset_session(self):
        """Make a new session"""
        # Get rid of any remaining bullets and aliens
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and recenter the ship
        self._create_fleet()
        self.ship.center_ship()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        while current_y < self.settings.screen_height - 4*alien_height:
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_alien_edge(self):
        """Respond appropriately if any alines have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_alien_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_star_sky(self):
        """Create the sky full of stars"""
        current_x, current_y = randint(0, 100), randint(0, 100)

        while current_y < self.settings.screen_height:
            while current_x < (self.settings.screen_width):

                self._create_star(current_x + randint(-100, 100),
                                  current_y + randint(-100, 100))
                current_x += 150

            current_x = randint(0, 100)
            current_y += 150

    def _create_star(self, x_position, y_position):
        """Create a star and place it in the row"""
        new_star = Star(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)

        # Draw the sky full of stars
        for star in self.stars.sprites():
            star.draw_star()

        # Draw the bullets before the ship, so they are not on the ship
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the play button if the game is in active
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    # print(ai.settings.screen_height, ai.settings.screen_width)
    ai.run_game()
