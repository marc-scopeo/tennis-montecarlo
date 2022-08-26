# Tennis Montecarlo simulation

This repo implements a Monte Carlo simulation of the tennis match. There are 3 parameters for each of the two players:
- The player's skill level represented by "strength" that directly affects the probability of winning a point.
- The player's capacity to win rewarding points (those which makes him win a set or a game) represented by "closing_strength_factor" that applies to the probability of winning a point as a multiplier of strength.
- The player's capacity to defend against rewarding points (those which makes the opponent win a set or a game) represented by "surviving_strength_factor" that applies to the probability of winning a point as a multiplier of strength

 
The notebook Tennis_simulator show how to run the simulation.