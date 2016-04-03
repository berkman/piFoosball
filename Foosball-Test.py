#!/usr/bin/env python

from Foosball import FoosballMatch, FoosballTeam, FoosballPlayer
from random import randint

my_match = FoosballMatch(2, 5,
    FoosballTeam("Ohio", FoosballPlayer("Drew"), FoosballPlayer("Mike")),
    FoosballTeam("SLC", FoosballPlayer("Eric"), FoosballPlayer("Jedidiah"))
    )

print my_match.team1.display_team()
print my_match.team2.display_team()
#for i in range(20):
while my_match.winner is False:
    print my_match.display_score()

    scoring_team = randint(1,2)

    if scoring_team == 1:
        my_match.score_goal(my_match.team1)
    elif scoring_team == 2:
        my_match.score_goal(my_match.team2)

print my_match.team1.player1.wins
print my_match.team1.player2.wins
print my_match.team2.player1.wins
print my_match.team2.player2.wins

'''
pseudo code

create a match

loop
    has a team won the match? -- how do we determine this?
        yes
            break
        no
            pick a random team number
            that team scores a goal
'''
