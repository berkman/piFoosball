#!/usr/bin/env python

from Foosball import FoosballMatch, FoosballTeam, FoosballPlayer

my_match = FoosballMatch(2, 5,
    FoosballTeam("Ohio", FoosballPlayer("Drew"), FoosballPlayer("Mike")),
    FoosballTeam("SLC", FoosballPlayer("Eric"), FoosballPlayer("Jedidiah"))
    )

print my_match.team1.display_team()
print my_match.team2.display_team()

print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team2)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team2)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team2)
print my_match.display_score()

my_match.score_goal(my_match.team2)
print my_match.display_score()

my_match.score_goal(my_match.team2)
print my_match.display_score()

my_match.score_goal(my_match.team2)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()

my_match.score_goal(my_match.team1)
print my_match.display_score()
