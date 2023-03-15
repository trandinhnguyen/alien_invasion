import pygame
import sys


class Controller:
    """A class to control the game"""

    def __init__(self, ai_game) -> None:
        """Initialize the controller"""
        self.ai_game = ai_game

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Save high score
                self.ai_game.stats.save_high_score()
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
        mouse_clicked = self.ai_game.play_button.rect.collidepoint(mouse_pos)

        if mouse_clicked and not self.ai_game.game_active:
            self._start_game()

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ai_game.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ai_game.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ai_game.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ai_game.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            if self.ai_game.game_active:
                self.ai_game._fire_bullet()
            else:
                self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ai_game.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ai_game.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ai_game.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ai_game.ship.moving_down = False

    def _start_game(self):
        """Start game"""
        # Reset the game statistics
        self.ai_game.stats.reset_stats()
        self.ai_game.sb.prep_images()
        self.ai_game.game_active = True

        # Reset the game settings
        self.ai_game.settings.initialize_dynamic_settings()

        # Make a new level
        self.ai_game.new_level()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
