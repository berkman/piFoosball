#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)      # Broadcom chip-specific pin numbers


# Capture the Button Press (Goal)
IN_TEAM1_GOAL = 	8	# Goal sensor 1, Pi input pin
IN_TEAM2_GOAL = 	7	# Goal sensor 2, Pi input pin

# Send signal to a certain display (1, 2, 3 or 4)
OUT_TEAM1_WINS = 	18 	# Display 1, Pi output pin
OUT_TEAM1_SCORE = 	23 	# Display 2, Pi output pin

OUT_TEAM2_WINS = 	24 	# Display 4, Pi output pin
OUT_TEAM2_SCORE = 	25 	# Display 3, Pi output pin

# Setup the Pins
GPIO.setup(IN_TEAM1_GOAL, GPIO.IN)
GPIO.setup(IN_TEAM2_GOAL, GPIO.IN)
GPIO.setup(OUT_TEAM1_WINS, GPIO.OUT)
GPIO.setup(OUT_TEAM1_SCORE, GPIO.OUT)
GPIO.setup(OUT_TEAM2_WINS, GPIO.OUT)
GPIO.setup(OUT_TEAM2_SCORE, GPIO.OUT)
