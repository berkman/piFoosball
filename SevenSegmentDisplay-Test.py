#!/usr/bin/env python

import time
from SevenSegmentDisplay import SevenSegmentDisplay

my_display = SevenSegmentDisplay()

my_display.print_zero(18)
time.sleep(1)
my_display.clear_display(18)
time.sleep(.01)

my_display.print_one(18)
time.sleep(1)
my_display.clear_display(18)
time.sleep(.01)

my_display.print_two(18)
time.sleep(1)
my_display.clear_display(18)
time.sleep(.01)

my_display.print_three(18)
time.sleep(1)
my_display.clear_display(18)
time.sleep(.01)
