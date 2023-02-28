import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star in the sky"""

    def __init__(self, ai_game) -> None:
        """Initialize the star and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.star_color

        self.rect = pygame.Rect(
            0, 0, self.settings.star_width, self.settings.star_height)

    def draw_star(self):
        """Draw the star to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
