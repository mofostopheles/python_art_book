# -*- coding: utf8 -*-
"""
	• A simple kind of pattern generation, output to console.
	• Author: Arlo Emerson <arloemerson@gmail.com>
	• License: GNU Lesser General Public License
"""

from decimal import Decimal
import math

def pattern_002():
# Simple pattern generation using division and string matching.

	# Parameters
	pattern_match = 9
	number_generator = math.e
	range_start = 1
	range_end = 10000
	print_string = ''
	display_char = '•'
	whitespace = ' '

	# Looping logic and string building
	for i in range(range_start, range_end):
		candidate = Decimal(i/number_generator) % 1
		if str(candidate).find(str(pattern_match)) > -1:
			print_string += display_char
		else: 
			print_string += whitespace

	# Send the string to the console
	print(print_string)

# Run the code
pattern_002()
