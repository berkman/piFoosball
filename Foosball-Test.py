#!/usr/bin/env python

from Foosball import FoosballMatch, FoosballTeam

my_match = FoosballMatch(2, 5, FoosballTeam("mike"), FoosballTeam("drew"))

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
