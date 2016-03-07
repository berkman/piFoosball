#!/usr/bin/env python

import RPi.GPIO as GPIO, time
import SevenSegmentDisplay

'''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
'''

my_display = SevenSegmentDisplay()

# Max score and wins
MAX_SCORE = 		5
MAX_WINS =			2


# Capture the Button Press (Goal)
IN_TEAM1_GOAL = 	8	# Goal sensor 1, Pi input pin
IN_TEAM2_GOAL = 	7	# Goal sensor 2, Pi input pin

# Send signal to a certain display (1, 2, 3 or 4)
OUT_TEAM1_WINS = 	18 	# Display 1, Pi output pin
OUT_TEAM1_SCORE = 	23 	# Display 2, Pi output pin

OUT_TEAM2_WINS = 	24 	# Display 4, Pi output pin
OUT_TEAM2_SCORE = 	25 	# Display 3, Pi output pin

TEAM1_WINS = 		0	# Number of games won by team 1
TEAM1_SCORE = 		0	# Number of goals by team 1
TEAM2_WINS = 		0	# Number of games won by team 2
TEAM2_SCORE = 		0	# Number of goals by team 2



# Setup the Pins
GPIO.setup(IN_TEAM1_GOAL, GPIO.IN)
GPIO.setup(IN_TEAM2_GOAL, GPIO.IN)
GPIO.setup(OUT_TEAM1_WINS, GPIO.OUT)
GPIO.setup(OUT_TEAM1_SCORE, GPIO.OUT)
GPIO.setup(OUT_TEAM2_WINS, GPIO.OUT)
GPIO.setup(OUT_TEAM2_SCORE, GPIO.OUT)



# Begin Logic
my_display.clear(OUT_TEAM1_WINS)
my_display.clear(OUT_TEAM1_SCORE)
my_display.clear(OUT_TEAM2_SCORE)
my_display.clear(OUT_TEAM2_WINS)


while True:
	if GPIO.input(IN_TEAM1_GOAL):		# Team 1 scores a goal
		TEAM1_SCORE += 1

		if TEAM1_SCORE >= MAX_SCORE and TEAM2_SCORE == 0 and TEAM2_WINS == 0:	# Skunk rule
			TEAM1_SCORE = 	0
			TEAM2_SCORE = 	0
			TEAM1_WINS = 	0
			TEAM2_WINS = 	0
		elif TEAM1_SCORE >= MAX_SCORE:
			TEAM1_SCORE = 	0
			TEAM2_SCORE = 	0
			TEAM1_WINS += 	1

		if TEAM1_WINS >= MAX_WINS:
			TEAM1_SCORE = 	0
			TEAM1_WINS = 	0
			TEAM2_SCORE = 	0
			TEAM2_WINS = 	0

		time.sleep(.5)
	elif GPIO.input(IN_TEAM2_GOAL):		# Team 2 scores a goal
		TEAM2_SCORE += 1

		if TEAM2_SCORE >= MAX_SCORE and TEAM1_SCORE == 0 and TEAM1_WINS == 0:	# Skunk rule
			TEAM1_SCORE = 	0
			TEAM2_SCORE = 	0
			TEAM1_WINS = 	0
			TEAM2_WINS = 	0
		elif TEAM2_SCORE >= MAX_SCORE:
			TEAM1_SCORE = 	0
			TEAM2_SCORE = 	0
			TEAM2_WINS += 	1

		if TEAM2_WINS >= MAX_WINS:
			TEAM1_SCORE = 	0
			TEAM1_WINS = 	0
			TEAM2_SCORE = 	0
			TEAM2_WINS = 	0

		time.sleep(.5)


	my_display.flash_digit(OUT_TEAM1_WINS,TEAM1_WINS, 0.001)
	my_display.flash_digit(OUT_TEAM1_SCORE,TEAM1_SCORE, 0.001)
	my_display.flash_digit(OUT_TEAM2_SCORE,TEAM2_SCORE, 0.001)
	my_display.flash_digit(OUT_TEAM2_WINS,TEAM2_WINS, 0.001)
