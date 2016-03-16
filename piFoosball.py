#!/usr/bin/env python

import RPi.GPIO as GPIO
from SevenSegmentDisplay import SevenSegmentDisplay
from Foosball import FoosballMatch, FoosballTeam

# Capture the Button Press (Goal)
team_1_goal = 8	# Goal sensor 1, Pi input pin
team_2_goal = 7	# Goal sensor 2, Pi input pin

# Set up the Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(team_1_goal, GPIO.IN)
GPIO.setup(team_2_goal, GPIO.IN)

# Set up the displays
duration = 1
team_1_wins = SevenSegmentDisplay(18)
team_1_score = SevenSegmentDisplay(23)
team_2_wins = SevenSegmentDisplay(24)
team_2_score = SevenSegmentDisplay(25)

my_match = FoosballMatch(2, 5, FoosballTeam("mike"), FoosballTeam("drew"))

my_match.score_goal(my_match.team1)

team_1_wins.flash_digit(my_match.team1.wins, duration)
team_1_score.flash_digit(my_match.team1.score, duration)
team_2_wins.flash_digit(my_match.team2.wins, duration)
team_2_score.flash_digit(my_match.team2.score, duration)
