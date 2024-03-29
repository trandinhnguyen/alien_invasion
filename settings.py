class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self) -> None:
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        # self.bg_color = (135, 206, 235)
        self.bg_color = (11, 16, 38)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 1000

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.05

        # How quickly the alien point values increase
        self.score_scale = 1.5

        # Star settings
        self.star_color = (255, 255, 0)
        self.star_width = 2
        self.star_height = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 3.0
        self.bullet_speed = 5.0
        self.alien_speed = 2.0
        self.shooting_period = 200_000_000  # nano second

        # Fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.shooting_period /= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
