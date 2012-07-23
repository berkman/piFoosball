#!/usr/bin/env python

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM);
GPIO.setwarnings(False);


# Capture the Button Press (Goal)
IN_TEAM1_GOAL = 	8;	# Goal sensor 1, Pi input pin
IN_TEAM2_GOAL = 	7;	# Goal sensor 2, Pi input pin

# Send signal to a certain display (1, 2, 3 or 4)
OUT_TEAM1_WINS = 	18; 	# Display 1, Pi output pin
OUT_TEAM1_SCORE = 	23; 	# Display 2, Pi output pin

OUT_TEAM2_WINS = 	24; 	# Display 4, Pi output pin
OUT_TEAM2_SCORE = 	25; 	# Display 3, Pi output pin

TEAM1_WINS = 		0;	# Number of games won by team 1
TEAM1_SCORE = 		0;	# Number of goals by team 1
TEAM2_WINS = 		0;	# Number of games won by team 2
TEAM2_SCORE = 		0;	# Number of goals by team 2

# 7-segment Pin mapping
SEG_A = 		4;	# Top middle segment
SEG_B = 		17;	# Top right segment
SEG_C = 		21;	# Bottom right segment
SEG_D = 		22;	# Bottom middle segment
SEG_E = 		10;	# Bottom left segment
SEG_F = 		9;	# Top left segment
SEG_G = 		11;	# Middle segment
SEG_PER = 		15;	# Period segment

# Setup the Pins
GPIO.setup(IN_TEAM1_GOAL, GPIO.IN);
GPIO.setup(IN_TEAM2_GOAL, GPIO.IN);

GPIO.setup(OUT_TEAM1_WINS, GPIO.OUT);
GPIO.setup(OUT_TEAM1_SCORE, GPIO.OUT);
GPIO.setup(OUT_TEAM2_WINS, GPIO.OUT);
GPIO.setup(OUT_TEAM2_SCORE, GPIO.OUT);
GPIO.setup(SEG_A, GPIO.OUT);
GPIO.setup(SEG_B, GPIO.OUT);
GPIO.setup(SEG_C, GPIO.OUT);
GPIO.setup(SEG_D, GPIO.OUT);
GPIO.setup(SEG_E, GPIO.OUT);
GPIO.setup(SEG_F, GPIO.OUT);
GPIO.setup(SEG_G, GPIO.OUT);


while 1: 
	if GPIO.input(IN_TEAM1_GOAL):
		print "GOAL! -- TEAM 1";
	elseif GPIO.input(IN_TEAM2_GOAL):
		print "GOAL! -- TEAM 2";
	else:	
		print "nothing";
