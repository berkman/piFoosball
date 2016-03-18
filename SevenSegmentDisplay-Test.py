#!/usr/bin/env python

from SevenSegmentDisplay import SevenSegmentDisplay

my_display_pins = [18, 23, 24, 25]
duration = .1

for display_pin in my_display_pins:
	my_display = SevenSegmentDisplay(display_pin)

	my_display.flash_digit('0', duration)
	my_display.flash_digit('1', duration)
	my_display.flash_digit('2', duration)
	my_display.flash_digit('3', duration)
	my_display.flash_digit('4', duration)
	my_display.flash_digit('5', duration)
	my_display.flash_digit('6', duration)
	my_display.flash_digit('7', duration)
	my_display.flash_digit('8', duration)
	my_display.flash_digit('9', duration)
	my_display.flash_digit('-', duration)
	my_display.flash_digit('.', duration)
