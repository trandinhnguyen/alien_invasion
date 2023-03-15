from pathlib import Path


class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game) -> None:
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset
        path = Path('high_score.txt')
        try:
            self.high_score = int(path.read_text())
        except FileNotFoundError:
            self.high_score = 0
        except ValueError:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Save the high score to a file"""
        path = Path('high_score.txt')
        path.write_text(str(self.high_score))
