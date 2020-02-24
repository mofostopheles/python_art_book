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

def pattern_023():
# Simple pattern generation using division and string matching.

	source_numbers = [53, 279, 505, 731, 957, 1183, 1409, 1635, 1861, 2087, 2313, 2539, 2765, 2991, 3217, 3443, 3669, 3895, 4121, 4347, 4573, 4799, 5025, 5251, 5477, 5703, 5929, 6155, 6381, 6607, 6833, 7059, 7285, 7511, 7737, 7963, 8189, 8415, 8641, 8867, 9093, 9319, 9545, 9771, 9997]
	display_char = '.'
	another_set = []

	for i in source_numbers:
		another_set.append(math.sqrt(i)*1.81)

	# Chart setup and display
	_common.chart_setup(plt)
	plt.xlabel('source numbers, N')
	plt.ylabel('Sq Root of N * 1.81')
	plt.scatter(source_numbers, another_set, marker=display_char)
	plt.title(_common.function_name(), fontsize=14)
	plt.savefig( _common.PATH_TO_PLOTS + \
				 _common.function_name() + \
				 '.png')
	plt.show()
	plt.clf()

# Run the code
pattern_023()
