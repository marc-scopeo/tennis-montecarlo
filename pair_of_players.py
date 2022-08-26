import numpy as np


class PairOfPlayers:
    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b

    def is_tie_break(self):
        if self.player_a.games == 6 and self.player_b.games == 6:
            if self.player_a.sets + self.player_b.sets == 4:
                return False
            else:
                return True
        else:
            return False

    def play_one_match(self):
        self.player_a.reset_before_new("match")
        self.player_b.reset_before_new("match")
        while self.player_a.sets < 3 and self.player_b.sets < 3:
            self.play_one_set()
        if self.player_a.sets > self.player_b.sets:
            self.player_a.matchs += 1
        else:
            self.player_b.matchs += 1

    def play_one_set(self):
        self.player_a.reset_before_new("set")
        self.player_b.reset_before_new("set")
        while not (
            (self.player_a.games >= 6 or self.player_b.games >= 6)
            and np.abs(self.player_a.games - self.player_b.games) >= 2
        ):
            self.play_one_game(self.is_tie_break())
        if self.player_a.games > self.player_b.games:
            self.player_a.sets += 1
        else:
            self.player_b.sets += 1

    def play_one_game(self, is_tie_break):
        self.player_a.reset_before_new("game")
        self.player_b.reset_before_new("game")
        limit = 4 + 2 * is_tie_break
        while not (
            (self.player_a.points >= limit or self.player_b.points >= limit)
            and np.abs(self.player_a.points - self.player_b.points) >= 2
        ):
            self.play_one_point(limit)
        if self.player_a.points > self.player_b.points:
            self.player_a.games += 1
        else:
            self.player_b.games += 1

    def _game_point(self, limit):
        equal_score = self.player_a.points == self.player_b.points
        if (self.player_a.points >= (limit - 1)) and not equal_score:
            return True, False
        if (self.player_b.points >= (limit - 1)) and not equal_score:
            return False, True
        return False, False

    def play_one_point(self, limit=4):
        a_game_point, b_game_point = self._game_point(limit)
        a_strength = self.player_a.get_strength(closing=a_game_point, surviving=b_game_point)
        b_strength = self.player_b.get_strength(closing=b_game_point, surviving=a_game_point)
        proba_a_wins = a_strength / (a_strength + b_strength)
        a_wins = (np.random.randint(100) + 0.5) < (100 * proba_a_wins)
        self.player_a.points += a_wins
        self.player_b.points += 1 - a_wins

    def play_n_confrontations(self, n):
        self.player_a.reset_before_new()
        self.player_b.reset_before_new()
        for k in range(n):
            self.play_one_match()

    def print_scores(self):
        print(self.player_a.matchs, self.player_b.matchs)
