# -*- coding: utf8 -*-
"""
	• The simpliest kind of pattern generation using the print statement.
	• Author: Arlo Emerson <arloemerson@gmail.com>
	• License: GNU Lesser General Public License
"""

from decimal import Decimal
import math

def command_line_001():
# Simple pattern generation using division and string matching.

	# Parameters
	pattern_match = '77'
	number_generator = math.e
	print_string = ''
	display_char = '•'
	whitespace = ' '

	# Looping logic and string building
	for i in range(1, 10000):
		candidate = Decimal(i/number_generator) % 1
		if str(candidate).find(pattern_match) > -1:
			print_string += display_char
		else: 
			print_string += whitespace

	# Send the string to the console
	print(print_string)

# Run the code
command_line_001()
