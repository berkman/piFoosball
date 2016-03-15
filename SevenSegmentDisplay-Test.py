#!/usr/bin/env python

import time
from SevenSegmentDisplay import SevenSegmentDisplay

my_displays = [18, 23, 24, 25]
duration = .1

for display in my_displays:
	my_display = SevenSegmentDisplay(display)

	my_display.flash_digit(display, '0', duration)
	my_display.flash_digit(display, '1', duration)
	my_display.flash_digit(display, '2', duration)
	my_display.flash_digit(display, '3', duration)
	my_display.flash_digit(display, '4', duration)
	my_display.flash_digit(display, '5', duration)
	my_display.flash_digit(display, '6', duration)
	my_display.flash_digit(display, '7', duration)
	my_display.flash_digit(display, '8', duration)
	my_display.flash_digit(display, '9', duration)
	my_display.flash_digit(display, '-', duration)
	my_display.flash_digit(display, '.', duration)
