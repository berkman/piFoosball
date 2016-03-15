#!/usr/bin/env python

#import time

class FoosballTeam(object):
	wins =	0
	score = 0
	name = ""

	def __init__(self, name):
		self.wins = 0
		self.score = 0
		self.name = name

	def display_score(self):
		return "%d - %d" % (self.wins, self.score)

	def score_goal(self):
		self.score += 1

	def set_name(self, name):
		self.name = name

class FoosballGame(object):
	max_score = 5

	team1 = FoosballTeam("")
	team2 = FoosballTeam("")

	def __init__(self, max_score):
		self.max_score = max_score

	def display_score(self):
		return "%s(%d) : %s(%d)" % \
			(self.team1.name, self.team1.score, self.team2.name, self.team2.score)

	def win_game(self, team):
		team.wins += 1

		self.team1.score = 0
		self.team2.score = 0

		print "Winner!  Team %s" % team.name
		# increment wins?

	def score_goal(self, team):
		team.score_goal()

		if team.score >= self.max_score:
			self.win_game(team)

class FoosballMatch(object):
	max_wins =	2

	def __init__(self, max_wins):
		self.max_wins = max_wins

	def display_score(self):
		return "%d - %d : %d - %d" % \
			(self.team_1_wins, self.team_1_score, self.team_2_score, self.team_2_wins)


my_match = FoosballMatch(2)
my_game = FoosballGame(5)
my_game.team1.set_name("red")


print my_game.display_score()
my_game.score_goal(my_game.team1)
print my_game.display_score()
my_game.score_goal(my_game.team1)
print my_game.display_score()
my_game.score_goal(my_game.team1)
print my_game.display_score()
my_game.score_goal(my_game.team2)
print my_game.display_score()
my_game.score_goal(my_game.team1)
print my_game.display_score()
my_game.score_goal(my_game.team1)
print my_game.display_score()
my_game.score_goal(my_game.team1)
print my_game.display_score()
my_game.score_goal(my_game.team1)
print my_game.display_score()

print my_game.team1.wins
print my_game.team2.wins


'''
if TEAM1_SCORE >= MAX_SCORE and TEAM2_SCORE == 0 and TEAM2_WINS == 0:
	TEAM1_SCORE = 	0
	TEAM2_SCORE = 	0
	TEAM1_WINS = 	0
	TEAM2_WINS = 	0

if TEAM1_WINS >= MAX_WINS:
	TEAM1_SCORE = 	0
	TEAM1_WINS = 	0
	TEAM2_SCORE = 	0
	TEAM2_WINS = 	0
'''
