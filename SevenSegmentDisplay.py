import RPi.GPIO as GPIO
import time

class SevenSegmentDisplay(object):
    # what does this class do?

    # 7-segment Pin mapping
    SEG_A =     4	# Top middle segment
    SEG_B = 	17	# Top right segment
    SEG_C = 	21	# Bottom right segment
    SEG_D = 	22	# Bottom middle segment
    SEG_E = 	10	# Bottom left segment
    SEG_F = 	9	# Top left segment
    SEG_G = 	11	# Middle segment
    SEG_PER = 	15	# Period segment


    def __init__(self):
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

        GPIO.setup(18, GPIO.OUT)

    # Set all segments to off
    def clear_display(self, display):
    	GPIO.output(display, GPIO.HIGH)

    # Print 0
    def print_zero(self, display):
    	GPIO.output(display, GPIO.LOW)         # Enable display
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.LOW)
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 1
    def print_one(self, display):
    	GPIO.output(display, GPIO.LOW)		   # Enable display
    	GPIO.output(self.SEG_A, GPIO.LOW)
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.LOW)
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 2
    def print_two(self, display):
    	GPIO.output(display, GPIO.LOW)		   # Enable display
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.LOW)
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 3
    def print_three(self, display):
    	GPIO.output(display, GPIO.LOW)		   # Enable display
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 4
    def print_four(self, display):
    	GPIO.output(display, GPIO.LOW)		   # Enable display
    	GPIO.output(self.SEG_A, GPIO.LOW)
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 5
    def print_five(self, display):
    	GPIO.output(display, GPIO.LOW)		   # Enable display
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.LOW)
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 6
    def print_six(self, display):
    	GPIO.output(display, GPIO.LOW)		   # Enable display
    	GPIO.output(self.SEG_A, GPIO.LOW)
    	GPIO.output(self.SEG_B, GPIO.LOW)
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 7
    def print_seven(self, display):
    	GPIO.output(display, GPIO.LOW)		   # Enable display
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.LOW)
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 8
    def print_eight(self, display):
    	GPIO.output(display, GPIO.LOW)         # Enable display
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_E, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print 9
    def print_nine(self, display):
    	GPIO.output(display, GPIO.LOW)		   # Enable display
    	GPIO.output(self.SEG_A, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_B, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_C, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_G, GPIO.HIGH)     # Light up
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print Dash
    def print_dash(self, display):
    	GPIO.output(display, GPIO.LOW)
    	GPIO.output(self.SEG_A, GPIO.LOW)
    	GPIO.output(self.SEG_B, GPIO.LOW)
    	GPIO.output(self.SEG_C, GPIO.LOW)
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.HIGH)
    	GPIO.output(self.SEG_PER, GPIO.LOW)

    # Print Period
    def print_period(self, display):
    	GPIO.output(display, GPIO.LOW)
    	GPIO.output(self.SEG_A, GPIO.LOW)
    	GPIO.output(self.SEG_B, GPIO.LOW)
    	GPIO.output(self.SEG_C, GPIO.LOW)
    	GPIO.output(self.SEG_D, GPIO.LOW)
    	GPIO.output(self.SEG_E, GPIO.LOW)
    	GPIO.output(self.SEG_F, GPIO.LOW)
    	GPIO.output(self.SEG_G, GPIO.LOW)
    	GPIO.output(self.SEG_PER, GPIO.HIGH)

    def flash_digit(self, display, value, duration):
    	if value == '0':
    		self.print_zero(display)
    	elif value == '1':
    		self.print_one(display)
    	elif value == '2':
    		self.print_two(display)
    	elif value == '3':
    		self.print_three(display)
    	elif value == '4':
    		self.print_four(display)
    	elif value == '5':
    		self.print_five(display)
    	elif value == '6':
    		self.print_six(display)
    	elif value == '7':
    		self.print_seven(display)
    	elif value == '8':
    		self.print_eight(display)
    	elif value == '9':
    		self.print_nine(display)
    	elif value == '-':
    		self.print_dash(display)
    	elif value == '.':
    		self.print_period(display)
    	else:
        	self.clear_display(display)

    	time.sleep(duration)
        self.clear_display(display)
