# -*- coding: utf8 -*-
"""
	• Using matplotlib to display number patterns.
	• Author: Arlo Emerson <arloemerson@gmail.com>
	• License: GNU Lesser General Public License
"""

from decimal import Decimal
import math
import matplotlib.pyplot as plt
import lib.common as _common

def pattern_022_generator():
# Simple pattern generation using division and string matching.


	# Parameters
	j = 808
	pattern_match = 314159
	number_generator = 1.0 + j/1000
	range_start = 1
	range_end = 10000
	display_char = '.'

	# Lists for each axis
	list_of_candidates = []
	list_of_numbers = []

	# # Looping logic and string building
	for i in range(range_start, range_end):
		candidate = Decimal(i/number_generator) % 1
		if str(candidate).find( str(pattern_match) ) > -1:
			list_of_candidates.append( candidate )
			list_of_numbers.append( i )
			print(str(i) + ' ' + str(_common.is_prime(i)))


	# Chart setup and display
	if len(list_of_candidates) > 0: # don't plot if no values
		_common.chart_setup(plt)
		plt.xlabel('Occurances of ' + \
					str(pattern_match) + \
					" within N÷" + \
					str(round(number_generator, 2)) )
		plt.ylabel('Range of N')
		plt.scatter(list_of_candidates, list_of_numbers, marker=display_char)
		plt.title(_common.function_name(), fontsize=14)
		plt.savefig( _common.PATH_TO_PLOTS + \
					 _common.function_name() + \
					 '-' + str(pattern_match) + \
					 '-' + str(round(number_generator, 3)) + \
					 '-' + str(j) + \
					 '.png')
		# plt.show() # commented out, otherwise you will need to manually dismiss each new plot
		plt.clf()

# Run the code
pattern_022_generator()
