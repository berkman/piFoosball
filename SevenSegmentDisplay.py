import RPi.GPIO as GPIO, time

class SevenSegmentDisplay(object):
    # what does this class do?

    # 7-segment Pin mapping
    SEG_A = 			4	# Top middle segment
    SEG_B = 			17	# Top right segment
    SEG_C = 			21	# Bottom right segment
    SEG_D = 			22	# Bottom middle segment
    SEG_E = 			10	# Bottom left segment
    SEG_F = 			9	# Top left segment
    SEG_G = 			11	# Middle segment
    SEG_PER = 			15	# Period segment

    def __init__(self):
        # setup display
        GPIO.setup(SEG_A, GPIO.OUT)
        GPIO.setup(SEG_B, GPIO.OUT)
        GPIO.setup(SEG_C, GPIO.OUT)
        GPIO.setup(SEG_D, GPIO.OUT)
        GPIO.setup(SEG_E, GPIO.OUT)
        GPIO.setup(SEG_F, GPIO.OUT)
        GPIO.setup(SEG_G, GPIO.OUT)

    # Set all segments to off
    def clear_display(display):
    	GPIO.output(display, GPIO.HIGH)

    # Print 0
    def print_zero(display):
    	GPIO.output(display, GPIO.LOW)		# Enable display
    	GPIO.output(SEG_A, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_B, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_C, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_D, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_E, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_F, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_G, GPIO.LOW)

    # Print 1
    def print_one(display):
    	GPIO.output(display, GPIO.LOW)		# Enable display
    	GPIO.output(SEG_A, GPIO.LOW)
    	GPIO.output(SEG_B, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_C, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_D, GPIO.LOW)
    	GPIO.output(SEG_E, GPIO.LOW)
    	GPIO.output(SEG_F, GPIO.LOW)
    	GPIO.output(SEG_G, GPIO.LOW)

    # Print 2
    def print_two(display):
    	GPIO.output(display, GPIO.LOW)		# Enable display
    	GPIO.output(SEG_A, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_B, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_C, GPIO.LOW)
    	GPIO.output(SEG_D, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_E, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_F, GPIO.LOW)
    	GPIO.output(SEG_G, GPIO.HIGH)		# Light up

    # Print 3
    def print_three(display):
    	GPIO.output(display, GPIO.LOW)		# Enable display
    	GPIO.output(SEG_A, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_B, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_C, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_D, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_E, GPIO.LOW)
    	GPIO.output(SEG_F, GPIO.LOW)
    	GPIO.output(SEG_G, GPIO.HIGH)		# Light up

    # Print 4
    def print_four(display):
    	GPIO.output(display, GPIO.LOW)		# Enable display
    	GPIO.output(SEG_A, GPIO.LOW)
    	GPIO.output(SEG_B, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_C, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_D, GPIO.LOW)
    	GPIO.output(SEG_E, GPIO.LOW)
    	GPIO.output(SEG_F, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_G, GPIO.HIGH)		# Light up

    # Print 5
    def print_five(display):
    	GPIO.output(display, GPIO.LOW)		# Enable display
    	GPIO.output(SEG_A, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_B, GPIO.LOW)
    	GPIO.output(SEG_C, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_D, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_E, GPIO.LOW)
    	GPIO.output(SEG_F, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_G, GPIO.HIGH)		# Light up

    # Print 6
    def print_six(display):
    	GPIO.output(display, GPIO.LOW)		# Enable display
    	GPIO.output(SEG_A, GPIO.LOW)
    	GPIO.output(SEG_B, GPIO.LOW)
    	GPIO.output(SEG_C, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_D, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_E, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_F, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_G, GPIO.HIGH)		# Light up

    # Print 7
    def print_seven(display):
    	GPIO.output(display, GPIO.LOW)		# Enable display
    	GPIO.output(SEG_A, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_B, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_C, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_D, GPIO.LOW)
    	GPIO.output(SEG_E, GPIO.LOW)
    	GPIO.output(SEG_F, GPIO.LOW)
    	GPIO.output(SEG_G, GPIO.LOW)

    # Print 8
    def print_eight(display):
    	GPIO.output(display, GPIO.LOW)		# Enable display
    	GPIO.output(SEG_A, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_B, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_C, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_D, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_E, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_F, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_G, GPIO.HIGH)		# Light up

    # Print 9
    def print_nine(display):
    	GPIO.output(display, GPIO.LOW)		# Enable display
    	GPIO.output(SEG_A, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_B, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_C, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_D, GPIO.LOW)
    	GPIO.output(SEG_E, GPIO.LOW)
    	GPIO.output(SEG_F, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_G, GPIO.HIGH)		# Light up

    # Print Dash TODO
    def print_dash(display):
    	GPIO.output(display, GPIO.LOW)		# Enable display
    	GPIO.output(SEG_A, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_B, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_C, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_D, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_E, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_F, GPIO.HIGH)		# Light up
    	GPIO.output(SEG_G, GPIO.LOW)

    def flash_digit(display, value, duration):
    	if value == 1:
    		print_one(display)
    	elif value == 2:
    		print_two(display)
    	elif value == 3:
    		print_three(display)
    	elif value == 4:
    		print_four(display)
    	elif value == 5:
    		print_five(display)
    	elif value == 6:
    		print_six(display)
    	elif value == 7:
    		print_seven(display)
    	elif value == 8:
    		print_eight(display)
    	elif value == 9:
    		print_nine(display)
    	else:
    		print_zero(display)

    	time.sleep(duration)
        clear_display(display)
