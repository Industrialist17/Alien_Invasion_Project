class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai):
        """Initialize statistics."""
        self.settings=ai.settings
        self.reset_stats()

        #High score should never be reset.
        self.high_score=0
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left=self.settings.ship_limit
        self.score=0
        self.level=1
        self.aliens_killed=0
   