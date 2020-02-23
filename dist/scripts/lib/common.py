# -*- coding: utf8 -*-
"""
	• Commonly used items.
	• Usage: import lib.common as _common
	• Usage: if _common.isPrime(i): # ...
	• Author: Arlo Emerson <arloemerson@gmail.com>
	• License: GNU Lesser General Public License
"""

import inspect

RED = '\033[91m'
END = '\033[0m'
PATH_TO_PLOTS = '../../__render/plots/'

def isPrime(number):
	if (number==1):
		return False
	elif (number==2):
		return True;
	else:
		for i in range(2,number):
			if(number % i==0):
				return False
		return True 

def reduce(number):
	input_number = str(number)
	value = 0
	for i in input_number:
		value += int(i)

	if (value > 9):
		return reduce(value)
	else:
		return value

def chart_setup(plot):
	# list the plot styles
	# print(plot.style.available)

	# set the style
	plot.style.use('seaborn-dark-palette')
	plot.style.use('seaborn-whitegrid')
		
def function_name():
	return inspect.stack()[1].function
