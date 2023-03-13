class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self) -> None:
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        # self.bg_color = (135, 206, 235)
        self.bg_color = (11, 16, 38)

        # ship settings
        self.ship_speed = 2.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 100

        # Alien settings
        self.alien_speed = 2.5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        # Star settings
        self.star_color = (255, 255, 0)
        self.star_width = 2
        self.star_height = 2
