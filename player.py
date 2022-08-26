class Player:
    def __init__(self, strength, closing_strength_factor=1.0, surviving_strength_factor=1.0):
        self._strength = strength
        self._closing_strength_factor = closing_strength_factor
        self._surviving_strength_factor = surviving_strength_factor

        self.points = 0
        self.games = 0
        self.sets = 0
        self.matchs = 0

    def reset_before_new(self, stage=""):
        self.points = 0
        if stage == "game":
            return
        self.games = 0
        if stage == "set":
            return
        self.sets = 0
        if stage == "match":
            return
        self.matchs = 0

    def get_strength(self, closing=False, surviving=False):
        strength = self._strength
        if closing:
            strength *= self._closing_strength_factor
        if surviving:
            strength *= self._surviving_strength_factor
        return strength
