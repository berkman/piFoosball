class FoosballPlayer(object):
	pass

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

	def __init__(self, max_score, team1=FoosballTeam(""), team2=FoosballTeam("")):
		self.max_score = max_score
		self.team1 = team1
		self.team2 = team2

	def display_score(self):
		return "%s(%d) : %s(%d)" % \
			(self.team1.name, self.team1.score, self.team2.name, self.team2.score)

	def win_game(self, team):
		team.wins += 1

		# TODO - make a reset function?
		self.team1.score = 0
		self.team2.score = 0

		print "Game Winner!  Team %s" % team.name

	def score_goal(self, team):
		team.score_goal()

		if team.score >= self.max_score:
			self.win_game(team)

class FoosballMatch(object):
	max_wins = 2

	team1 = FoosballTeam("")
	team2 = FoosballTeam("")

	game = FoosballGame(0)

	def __init__(self, max_wins, max_score, team1=FoosballTeam(""), team2=FoosballTeam("")):
		#TODO - must be more than 1 match, 1 game
		self.max_wins = max_wins
		self.team1 = team1
		self.team2 = team2
		self.game = FoosballGame(max_score, self.team1, self.team2)

	def display_score(self):
		return "%s(%d) %d : %d %s(%d)" % \
			(self.team1.name, self.team1.wins, self.team1.score,
			self.team2.score, self.team2.name, self.team2.wins)

	def score_goal(self, team):
		self.game.score_goal(team)

		if team.wins >= self.max_wins:
			self.win_match(team)

	def win_match(self, team):
		# TODO - make a reset function?
		self.team1.wins = 0
		self.team2.wins = 0

		print "Match Winner!  Team %s" % team.name
