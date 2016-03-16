import RPi.GPIO as GPIO
import time

class SevenSegmentDisplay(object):
    # what does this class do?

    # 7-segment Pin mapping
    segment_a = 0	# Top middle segment
    segment_b = 0	# Top right segment
    segment_c = 0   # Bottom right segment
    segment_d = 0	# Bottom middle segment
    segment_e = 0	# Bottom left segment
    segment_f = 0   # Top left segment
    segment_g = 0	# Middle segment
    segment_p = 0	# Period segment

    display_pin = 0

    def __init__(self, display_pin=18, a=4, b=17, c=1, d=22, e=10, f=9, g=11, p=15):
        self.display_pin = display_pin
        self.segment_a = a
        self.segment_b = b
        self.segment_c = c
        self.segment_d = d
        self.segment_e = e
        self.segment_f = f
        self.segment_g = g
        self.segment_p = p

        # setup display
        GPIO.setmode(GPIO.BCM)               # Broadcom chip-specific pin numbers
        GPIO.setwarnings(False)

        GPIO.setup(self.segment_a, GPIO.OUT)     # declare this PIN as an OUTPUT
        GPIO.setup(self.segment_b, GPIO.OUT)
        GPIO.setup(self.segment_c, GPIO.OUT)
        GPIO.setup(self.segment_d, GPIO.OUT)
        GPIO.setup(self.segment_e, GPIO.OUT)
        GPIO.setup(self.segment_f, GPIO.OUT)
        GPIO.setup(self.segment_g, GPIO.OUT)
        GPIO.setup(self.segment_p, GPIO.OUT)

        GPIO.setup(self.display_pin, GPIO.OUT)

    # Set all segments to off
    def clear_display(self):
    	GPIO.output(self.display_pin, GPIO.HIGH)

    # Print 0
    def print_zero(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.HIGH)
    	GPIO.output(self.segment_b, GPIO.HIGH)
    	GPIO.output(self.segment_c, GPIO.HIGH)
    	GPIO.output(self.segment_d, GPIO.HIGH)
    	GPIO.output(self.segment_e, GPIO.HIGH)
    	GPIO.output(self.segment_f, GPIO.HIGH)
    	GPIO.output(self.segment_g, GPIO.LOW)
    	GPIO.output(self.segment_p, GPIO.LOW)

    # Print 1
    def print_one(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.LOW)
    	GPIO.output(self.segment_b, GPIO.HIGH)
    	GPIO.output(self.segment_c, GPIO.HIGH)
    	GPIO.output(self.segment_d, GPIO.LOW)
    	GPIO.output(self.segment_e, GPIO.LOW)
    	GPIO.output(self.segment_f, GPIO.LOW)
    	GPIO.output(self.segment_g, GPIO.LOW)
    	GPIO.output(self.segment_p, GPIO.LOW)

    # Print 2
    def print_two(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.HIGH)
    	GPIO.output(self.segment_b, GPIO.HIGH)
    	GPIO.output(self.segment_c, GPIO.LOW)
    	GPIO.output(self.segment_d, GPIO.HIGH)
    	GPIO.output(self.segment_e, GPIO.HIGH)
    	GPIO.output(self.segment_f, GPIO.LOW)
    	GPIO.output(self.segment_g, GPIO.HIGH)
    	GPIO.output(self.segment_p, GPIO.LOW)

    # Print 3
    def print_three(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.HIGH)
    	GPIO.output(self.segment_b, GPIO.HIGH)
    	GPIO.output(self.segment_c, GPIO.HIGH)
    	GPIO.output(self.segment_d, GPIO.HIGH)
    	GPIO.output(self.segment_e, GPIO.LOW)
    	GPIO.output(self.segment_f, GPIO.LOW)
    	GPIO.output(self.segment_g, GPIO.HIGH)
    	GPIO.output(self.segment_p, GPIO.LOW)

    # Print 4
    def print_four(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.LOW)
    	GPIO.output(self.segment_b, GPIO.HIGH)
    	GPIO.output(self.segment_c, GPIO.HIGH)
    	GPIO.output(self.segment_d, GPIO.LOW)
    	GPIO.output(self.segment_e, GPIO.LOW)
    	GPIO.output(self.segment_f, GPIO.HIGH)
    	GPIO.output(self.segment_g, GPIO.HIGH)
    	GPIO.output(self.segment_p, GPIO.LOW)

    # Print 5
    def print_five(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.HIGH)
    	GPIO.output(self.segment_b, GPIO.LOW)
    	GPIO.output(self.segment_c, GPIO.HIGH)
    	GPIO.output(self.segment_d, GPIO.HIGH)
    	GPIO.output(self.segment_e, GPIO.LOW)
    	GPIO.output(self.segment_f, GPIO.HIGH)
    	GPIO.output(self.segment_g, GPIO.HIGH)
    	GPIO.output(self.segment_p, GPIO.LOW)

    # Print 6
    def print_six(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.LOW)
    	GPIO.output(self.segment_b, GPIO.LOW)
    	GPIO.output(self.segment_c, GPIO.HIGH)
    	GPIO.output(self.segment_d, GPIO.HIGH)
    	GPIO.output(self.segment_e, GPIO.HIGH)
    	GPIO.output(self.segment_f, GPIO.HIGH)
    	GPIO.output(self.segment_g, GPIO.HIGH)
    	GPIO.output(self.segment_p, GPIO.LOW)

    # Print 7
    def print_seven(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.HIGH)
    	GPIO.output(self.segment_b, GPIO.HIGH)
    	GPIO.output(self.segment_c, GPIO.HIGH)
    	GPIO.output(self.segment_d, GPIO.LOW)
    	GPIO.output(self.segment_e, GPIO.LOW)
    	GPIO.output(self.segment_f, GPIO.LOW)
    	GPIO.output(self.segment_g, GPIO.LOW)
    	GPIO.output(self.segment_p, GPIO.LOW)

    # Print 8
    def print_eight(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.HIGH)
    	GPIO.output(self.segment_b, GPIO.HIGH)
    	GPIO.output(self.segment_c, GPIO.HIGH)
    	GPIO.output(self.segment_d, GPIO.HIGH)
    	GPIO.output(self.segment_e, GPIO.HIGH)
    	GPIO.output(self.segment_f, GPIO.HIGH)
    	GPIO.output(self.segment_g, GPIO.HIGH)
    	GPIO.output(self.segment_p, GPIO.LOW)

    # Print 9
    def print_nine(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.HIGH)
    	GPIO.output(self.segment_b, GPIO.HIGH)
    	GPIO.output(self.segment_c, GPIO.HIGH)
    	GPIO.output(self.segment_d, GPIO.LOW)
    	GPIO.output(self.segment_e, GPIO.LOW)
    	GPIO.output(self.segment_f, GPIO.HIGH)
    	GPIO.output(self.segment_g, GPIO.HIGH)
    	GPIO.output(self.segment_p, GPIO.LOW)

    # Print Dash
    def print_dash(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.LOW)
    	GPIO.output(self.segment_b, GPIO.LOW)
    	GPIO.output(self.segment_c, GPIO.LOW)
    	GPIO.output(self.segment_d, GPIO.LOW)
    	GPIO.output(self.segment_e, GPIO.LOW)
    	GPIO.output(self.segment_f, GPIO.LOW)
    	GPIO.output(self.segment_g, GPIO.HIGH)
    	GPIO.output(self.segment_p, GPIO.LOW)

    # Print Period
    def print_period(self):
    	GPIO.output(self.display_pin, GPIO.LOW)
    	GPIO.output(self.segment_a, GPIO.LOW)
    	GPIO.output(self.segment_b, GPIO.LOW)
    	GPIO.output(self.segment_c, GPIO.LOW)
    	GPIO.output(self.segment_d, GPIO.LOW)
    	GPIO.output(self.segment_e, GPIO.LOW)
    	GPIO.output(self.segment_f, GPIO.LOW)
    	GPIO.output(self.segment_g, GPIO.LOW)
    	GPIO.output(self.segment_p, GPIO.HIGH)

    def flash_digit(self, value, duration):
    	if value == 0:
    		self.print_zero()
    	elif value == 1:
    		self.print_one()
    	elif value == 2:
    		self.print_two()
    	elif value == 3:
    		self.print_three()
    	elif value == 4:
    		self.print_four()
    	elif value == 5:
    		self.print_five()
    	elif value == 6:
    		self.print_six()
    	elif value == 7:
    		self.print_seven()
    	elif value == 8:
    		self.print_eight()
    	elif value == 9:
    		self.print_nine()
    	elif value == '-':
    		self.print_dash()
    	elif value == '.':
    		self.print_period()
    	else:
        	self.clear_display()

    	time.sleep(duration)
        self.clear_display()

class MultiDisplay(object):
    display_pin = 0

    def __init__(self, num_displays):
        pass
