# https://www.algoexpert.io/questions/Tournament%20Winner

from collections import defaultdict


def tournament_winner(competitions, results):
    scores = defaultdict(lambda: 0)
    winning_team = ""

    for idx, competition in enumerate(competitions):
        home_team, away_team = competition
        result = results[idx]

        current_winner = home_team if result == 1 else away_team
        scores[current_winner] += 3

        if scores[current_winner] > scores[winning_team]:
            winning_team = current_winner

    return winning_team


def test_0():
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]

    results = [0, 0, 1]

    assert tournament_winner(competitions, results) == "Python"
