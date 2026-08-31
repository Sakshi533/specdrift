Write a Python function `table(results)`.

`results` is a list of match tuples `(home, away, home_goals, away_goals)` —
team names are strings, goals are ints. A win is worth 3 points, a draw 1,
a loss 0. Return the league standings as a list of team names (every team
that appears in `results`), best first, ordered by:

1. points, descending
2. goal difference (goals scored minus goals conceded), descending
3. goals scored, descending
4. team name, ascending
