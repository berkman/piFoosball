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

# Set everything to off
def clear_all():
	GPIO.output(OUT_TEAM1_WINS, GPIO.HIGH);
	GPIO.output(OUT_TEAM1_SCORE, GPIO.HIGH);
	GPIO.output(OUT_TEAM2_WINS, GPIO.HIGH);
	GPIO.output(OUT_TEAM2_SCORE, GPIO.HIGH);

# Set everything to off
def clear_display(display):
	GPIO.output(display, GPIO.HIGH);

# Print 0
def print_zero(display):
	GPIO.output(display, GPIO.LOW);
	GPIO.output(SEG_A, GPIO.HIGH);
	GPIO.output(SEG_B, GPIO.HIGH);		# Light up
	GPIO.output(SEG_C, GPIO.HIGH);		# Light up
	GPIO.output(SEG_D, GPIO.HIGH);
	GPIO.output(SEG_E, GPIO.HIGH);
	GPIO.output(SEG_F, GPIO.HIGH);
	GPIO.output(SEG_G, GPIO.HIGH);

# Print 1
def print_one(display):
	GPIO.output(display, GPIO.LOW);
	GPIO.output(SEG_A, GPIO.LOW);
	GPIO.output(SEG_B, GPIO.HIGH);		# Light up
	GPIO.output(SEG_C, GPIO.HIGH);		# Light up
	GPIO.output(SEG_D, GPIO.LOW);
	GPIO.output(SEG_E, GPIO.LOW);
	GPIO.output(SEG_F, GPIO.LOW);
	GPIO.output(SEG_G, GPIO.LOW);

# Print 2
def print_two(display):
	GPIO.output(display, GPIO.LOW);
	GPIO.output(SEG_A, GPIO.HIGH);		# Light up
	GPIO.output(SEG_B, GPIO.HIGH);		# Light up
	GPIO.output(SEG_C, GPIO.LOW);
	GPIO.output(SEG_D, GPIO.HIGH);		# Light up
	GPIO.output(SEG_E, GPIO.HIGH);		# Light up
	GPIO.output(SEG_F, GPIO.LOW);
	GPIO.output(SEG_G, GPIO.HIGH);		# Light up

# Print 3
def print_three(display):
	GPIO.output(display, GPIO.LOW);		# Enable display
	GPIO.output(SEG_A, GPIO.HIGH);		# Light up
	GPIO.output(SEG_B, GPIO.HIGH);		# Light up
	GPIO.output(SEG_C, GPIO.HIGH);		# Light up
	GPIO.output(SEG_D, GPIO.HIGH);		# Light up
	GPIO.output(SEG_E, GPIO.LOW);
	GPIO.output(SEG_F, GPIO.LOW);
	GPIO.output(SEG_G, GPIO.HIGH);		# Light up

# Print 4
def print_four(display):
	GPIO.output(display, GPIO.LOW);		# Enable display
	GPIO.output(SEG_A, GPIO.LOW);
	GPIO.output(SEG_B, GPIO.HIGH);
	GPIO.output(SEG_C, GPIO.HIGH);
	GPIO.output(SEG_D, GPIO.LOW);
	GPIO.output(SEG_E, GPIO.LOW);
	GPIO.output(SEG_F, GPIO.HIGH);
	GPIO.output(SEG_G, GPIO.HIGH);

# Print 5
def print_five(display):
	GPIO.output(display, GPIO.LOW);
	GPIO.output(SEG_A, GPIO.HIGH);
	GPIO.output(SEG_B, GPIO.LOW);
	GPIO.output(SEG_C, GPIO.HIGH);
	GPIO.output(SEG_D, GPIO.HIGH);
	GPIO.output(SEG_E, GPIO.LOW);
	GPIO.output(SEG_F, GPIO.HIGH);
	GPIO.output(SEG_G, GPIO.HIGH);

# Print 6
def print_six(display):
	GPIO.output(display, GPIO.LOW);
	GPIO.output(SEG_A, GPIO.LOW);
	GPIO.output(SEG_B, GPIO.LOW);
	GPIO.output(SEG_C, GPIO.HIGH);
	GPIO.output(SEG_D, GPIO.HIGH);
	GPIO.output(SEG_E, GPIO.HIGH);
	GPIO.output(SEG_F, GPIO.HIGH);
	GPIO.output(SEG_G, GPIO.HIGH);

# Print 7
def print_seven(display):
	GPIO.output(display, GPIO.LOW);
	GPIO.output(SEG_A, GPIO.HIGH);
	GPIO.output(SEG_B, GPIO.HIGH);
	GPIO.output(SEG_C, GPIO.HIGH);
	GPIO.output(SEG_D, GPIO.LOW);
	GPIO.output(SEG_E, GPIO.LOW);
	GPIO.output(SEG_F, GPIO.LOW);
	GPIO.output(SEG_G, GPIO.LOW);

# Print 8
def print_eight(display):
	GPIO.output(display, GPIO.LOW);
	GPIO.output(SEG_A, GPIO.HIGH);
	GPIO.output(SEG_B, GPIO.HIGH);
	GPIO.output(SEG_C, GPIO.HIGH);
	GPIO.output(SEG_D, GPIO.HIGH);
	GPIO.output(SEG_E, GPIO.HIGH);
	GPIO.output(SEG_F, GPIO.HIGH);
	GPIO.output(SEG_G, GPIO.HIGH);

# Print 9
def print_nine(display):
	GPIO.output(display, GPIO.LOW);
	GPIO.output(SEG_A, GPIO.HIGH);
	GPIO.output(SEG_B, GPIO.HIGH);
	GPIO.output(SEG_C, GPIO.HIGH);
	GPIO.output(SEG_D, GPIO.LOW);
	GPIO.output(SEG_E, GPIO.LOW);
	GPIO.output(SEG_F, GPIO.HIGH);
	GPIO.output(SEG_G, GPIO.HIGH);






# Begin Logic



clear_all();


while True:
	print_one(OUT_TEAM1_WINS);
	time.sleep(1);
	clear_display(OUT_TEAM1_WINS);
	print_two(OUT_TEAM1_SCORE);
	time.sleep(1);
	clear_display(OUT_TEAM1_SCORE);
	print_three(OUT_TEAM2_SCORE);
	time.sleep(1);
	clear_display(OUT_TEAM2_SCORE);
	print_four(OUT_TEAM2_WINS);
	time.sleep(1);
	clear_display(OUT_TEAM2_WINS);
	print_five(OUT_TEAM1_WINS);
	time.sleep(1);
	clear_display(OUT_TEAM1_WINS);
	print_six(OUT_TEAM1_SCORE);
	time.sleep(1);
	clear_display(OUT_TEAM1_SCORE);
	print_seven(OUT_TEAM2_SCORE);
	time.sleep(1);
	clear_display(OUT_TEAM2_SCORE);
	print_eight(OUT_TEAM2_WINS);
	time.sleep(1);
	clear_display(OUT_TEAM2_WINS);
























#while 1: 
#	if GPIO.input(IN_TEAM1_GOAL):
#		print "GOAL! -- TEAM 1";
#	elif GPIO.input(IN_TEAM2_GOAL):
#		print "GOAL! -- TEAM 2";
#	else:	
#		print "nothing";
