import RPi.GPIO as GPIO
import time

class SevenSegmentDisplay(object):
    # what does this class do?

    # 7-segment Pin mapping
    SEG_A =     4	# Top middle segment
    SEG_B = 	17	# Top right segment
    SEG_C = 	1	# Bottom right segment
    SEG_D = 	22	# Bottom middle segment
    SEG_E = 	10	# Bottom left segment
    SEG_F = 	9	# Top left segment
    SEG_G = 	11	# Middle segment
    SEG_PER = 	15	# Period segment

    display_pin = 18


    def __init__(self, display_pin=18):
	self.display_pin = display_pin

        # setup display
        GPIO.setmode(GPIO.BCM)               # Broadcom chip-specific pin numbers
        GPIO.setwarnings(False)

        GPIO.setup(self.SEG_A, GPIO.OUT)     # declare this PIN as an OUTPUT
        GPIO.setup(self.SEG_B, GPIO.OUT)
        GPIO.setup(self.SEG_C, GPIO.OUT)
        GPIO.setup(self.SEG_D, GPIO.OUT)
        GPIO.setup(self.SEG_E, GPIO.OUT)
        GPIO.setup(self.SEG_F, GPIO.OUT)
        GPIO.setup(self.SEG_G, GPIO.OUT)
        GPIO.setup(self.SEG_PER, GPIO.OUT)

        GPIO.setup(self.display_pin, GPIO.OUT)

    # Set all segments to off
    def clear_display(self):
    	GPIO.output(self.display_pin, GPIO.HIGH)

    # Print 0
    def print_zero(self):
    	GPIO.output(self.display_pin, GPIO.LOW)         # Enable display_pin
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.LOW)
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 1
    def print_one(self):
    	GPIO.output(self.display_pin, GPIO.LOW)		   # Enable display_pin
    	GPIO.output(self.SEG_A, GPIO.LOW)
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.LOW)
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 2
    def print_two(self):
    	GPIO.output(self.display_pin, GPIO.LOW)		   # Enable display_pin
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.LOW)
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 3
    def print_three(self):
    	GPIO.output(self.display_pin, GPIO.LOW)		   # Enable display_pin
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 4
    def print_four(self):
    	GPIO.output(self.display_pin, GPIO.LOW)		   # Enable display_pin
    	GPIO.output(self.SEG_A, GPIO.LOW)
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 5
    def print_five(self):
    	GPIO.output(self.display_pin, GPIO.LOW)		   # Enable display_pin
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.LOW)
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 6
    def print_six(self):
    	GPIO.output(self.display_pin, GPIO.LOW)		   # Enable display_pin
    	GPIO.output(self.SEG_A, GPIO.LOW)
    	GPIO.output(self.SEG_B, GPIO.LOW)
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 7
    def print_seven(self):
    	GPIO.output(self.display_pin, GPIO.LOW)		   # Enable display_pin
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.LOW)
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 8
    def print_eight(self):
    	GPIO.output(self.display_pin, GPIO.LOW)         # Enable display_pin
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 9
    def print_nine(self):
    	GPIO.output(self.display_pin, GPIO.LOW)		   # Enable display_pin
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print Dash
    def print_dash(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.SEG_A, GPIO.LOW)
    	GPIO.output(self.SEG_B, GPIO.LOW)
    	GPIO.output(self.SEG_C, GPIO.LOW)
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.HIGH)
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print Period
    def print_period(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.SEG_A, GPIO.LOW)
    	GPIO.output(self.SEG_B, GPIO.LOW)
    	GPIO.output(self.SEG_C, GPIO.LOW)
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.LOW)
    	GPIO.output(self.SEG_PER, GPIO.HIGH)

    def flash_digit(self, value, duration):
    	if value == '0':
    		self.print_zero()
    	elif value == '1':
    		self.print_one()
    	elif value == '2':
    		self.print_two()
    	elif value == '3':
    		self.print_three()
    	elif value == '4':
    		self.print_four()
    	elif value == '5':
    		self.print_five()
    	elif value == '6':
    		self.print_six()
    	elif value == '7':
    		self.print_seven()
    	elif value == '8':
    		self.print_eight()
    	elif value == '9':
    		self.print_nine()
    	elif value == '-':
    		self.print_dash()
    	elif value == '.':
    		self.print_period()
    	else:
        	self.clear_display()

    	time.sleep(duration)
        self.clear_display()
