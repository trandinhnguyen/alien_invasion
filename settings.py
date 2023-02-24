class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self) -> None:
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (135, 206, 235)

        # ship settings
        self.ship_speed = 2.5

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5
        

