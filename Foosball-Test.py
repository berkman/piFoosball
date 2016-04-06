#!/usr/bin/env python

from Foosball import FoosballMatch, FoosballTeam, FoosballPlayer
from random import randint

players = [
    FoosballPlayer("Drew"),
    FoosballPlayer("Mike"),
    FoosballPlayer("Eric"),
    FoosballPlayer("Jedidiah"),
    FoosballPlayer("Alex"),
    FoosballPlayer("Christian")
    ]

## TODO: randomize the teams/pairings?  save to file?

for i in range(5):
    my_match = FoosballMatch(
        2,
        5,
        FoosballTeam("Ohio", players[0], players[1]),
        FoosballTeam("SLC", players[2], players[3])
        )

    print my_match.team1.display_team()
    print my_match.team2.display_team()

    while my_match.winner is False:
        print my_match.get_score()

        scoring_team = randint(1,2)

        if scoring_team == 1:
            my_match.score_goal(my_match.team1)
        elif scoring_team == 2:
            my_match.score_goal(my_match.team2)

    for player in players:
        print player.get_wins()


'''
-keep statistics not only for individual wins, but wins by pairing/team
-winners stay at table
'''
