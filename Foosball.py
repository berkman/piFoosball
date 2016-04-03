class FoosballPlayer(object):
	wins = 0
	name = ""

	#TODO:  save this information to file/database

	def __init__(self, name):
		self.wins = 0
		self.name = name

	def set_name(self, name):
		self.name = name

	def win_match(self):
		self.wins += 1

		print "Match Winner!  Player %s" % self.name

	def get_wins(self):
		return "%s:  %s win(s)" % (self.name, self.wins)

class FoosballTeam(object):
	wins =	0
	score = 0
	name = ""

	player1 = FoosballPlayer("")
	player2 = FoosballPlayer("")

	def __init__(self, name="", player1=FoosballPlayer(""), player2=FoosballPlayer("")):
		self.wins = 0
		self.score = 0
		self.name = name
		self.player1 = player1
		self.player2 = player2

	def display_score(self):
		return "%d - %d" % (self.wins, self.score)

	def display_team(self):
		return "Team %s:  %s and %s" % (self.name, self.player1.name, self.player2.name)

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

	winner = False

	def __init__(self, max_wins, max_score, team1=FoosballTeam(""), team2=FoosballTeam("")):
		#TODO - must be more than 1 match, 1 game
		self.max_wins = max_wins
		self.team1 = team1
		self.team2 = team2
		self.game = FoosballGame(max_score, self.team1, self.team2)
		self.winner = False

	def get_score(self):
		return "%s(%d) %d : %d %s(%d)" % \
			(self.team1.name, self.team1.wins, self.team1.score,
			self.team2.score, self.team2.name, self.team2.wins)

	def score_goal(self, team):
		self.game.score_goal(team)

		if team.wins >= self.max_wins:
			self.win_match(team)

	def win_match(self, team):
		self.winner = True

		# TODO - make a reset function?
		self.team1.wins = 0
		self.team2.wins = 0

		team.player1.win_match()
		team.player2.win_match()

		print "Match Winner!  Team %s" % team.name
