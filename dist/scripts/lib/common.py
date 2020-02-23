# -*- coding: utf8 -*-
"""
	• Commonly used items.
	• Usage: import lib.common as _common
	• Usage: if _common.isPrime(i): # ...
	• Author: Arlo Emerson <arloemerson@gmail.com>
	• License: GNU Lesser General Public License
"""

from decimal import Decimal
import math

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

def reduceNumber(number):
	return 2