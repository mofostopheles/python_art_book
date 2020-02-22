'''
MY NOTES - arlo emerson 2/13/2020
Scratch pad for learning plotting.

pylab is discouraged according to this link: http://queirozf.com/entries/matplotlib-pylab-pyplot-etc-what-s-the-different-between-these

this is probably one of my great masterpieces.

'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import inspect
from decimal import Decimal
import math
import time

def chart_setup():
	# list the plot styles
	# print(plt.style.available)

	# set the style
	plt.style.use('seaborn-dark-palette')
	plt.style.use('seaborn-darkgrid')


def show_sine():
	chart_setup()
	plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')

	# save plot as image
	plt.savefig('sine.png')
	plt.show()

def simple_scatter():
	chart_setup()
	foolist = [12,14,15,16,45,78,23,45]
	years = [10, 100, 30, 50, 23, 45, 6, 134]


	plt.scatter(foolist, years, marker='o')
	plt.show()

def quadratic_1():
	chart_setup()

	x = np.arange(0.0, 10.0, 0.01)
	plt.title(r"Quadratic Curve", fontsize=20)
	plt.plot(x, x ** 2, "g")
	plt.show()

def schuman_divider_algorithm():
	chart_setup()
	list_of_numbers = []
	list_of_markers = []

	for num in range(0,1001):
		list_of_numbers.append( Decimal(num/7.83) % 1 )
		list_of_markers.append( num )
		# print(str(num) + " " + str(num/7.83))

	plt.scatter(list_of_numbers, list_of_markers, marker='o')
	plt.savefig('schuman_divider_algorithm.png')
	plt.show()


def fourthirtytwo_divider_algorithm():
	chart_setup()
	list_of_numbers = []
	list_of_markers = []

	for num in range(0,1001):
		list_of_numbers.append( Decimal(num/432) % 1 )
		list_of_markers.append( num )
		# print(str(num) + " " + str(num/7.83))

	plt.scatter(list_of_numbers, list_of_markers, marker='o')
	plt.savefig('fourthirtytwo_divider_algorithm.png')
	plt.show()

def twoseventysevenonethree_divider_algorithm():
	chart_setup()
	list_of_numbers = []
	list_of_markers = []

	for num in range(0,1001):
		list_of_numbers.append( Decimal(num/2771392) % 1 )
		list_of_markers.append( num )

	plt.scatter(list_of_numbers, list_of_markers, marker='o')
	plt.savefig('twoseventysevenonethree_divider_algorithm.png')
	plt.show()

def twoseventyseven_divider_algorithm():
	chart_setup()
	list_of_numbers = []
	list_of_markers = []

	for num in range(0,1001):
		list_of_numbers.append( Decimal(num/277) % 1 )
		list_of_markers.append( num )

	plt.scatter(list_of_numbers, list_of_markers, marker='o')
	plt.savefig('twoseventyseven_divider_algorithm.png')
	plt.show()

def is_prime(pNum):
	return true

def is_factor_of(pNum):

	for num in [3,5,7,11,13,17,19]:

		if pNum % num == 0:
			return True

	return False

def benford_distribution():
	# https://phys.org/news/2009-05-pattern-prime.html
	chart_setup()
	list_of_numbers = []
	list_of_markers = []

	magic_number = 3.14

	for num in range(0,1001):
		candidate = Decimal(num/magic_number) % 1
		if str(candidate)[2:3] == '0':
			list_of_numbers.append( candidate )
			list_of_markers.append( num )
		# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	plt.scatter(list_of_numbers, list_of_markers, marker='.')
	plt.savefig('benford_distribution.png')
	plt.show()

def magicnumber_divider_algorithm():
	chart_setup()
	list_of_numbers = []
	list_of_markers = []

	magic_number = 7.83

	for num in range(0,1000001):
		candidate = Decimal(num/magic_number) % 1
		# subcandidate = str(candidate)[2:5]

		if str(candidate).find( '999' ) > -1:
			print(candidate)
			list_of_numbers.append( candidate )
			list_of_markers.append( num )
		# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	plt.scatter(list_of_numbers, list_of_markers, marker='.')
	plt.savefig('magicnumber_divider_algorithm.png')
	plt.show()

# the quest for randomness series
def qfr_1():
	
	

	img = mpimg.imread('small_chick.png')

	# for i in range(1, 100):

	magic_number = math.e
	query_number = ''
	query_number_list = range(123,456)
	# query_number = str(i*math.floor(magic_number))
	candidate = ''

	for qn in query_number_list:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

		if len(list_of_numbers) > 0:
			chart_setup()
			plt.scatter(list_of_numbers, list_of_markers, marker='.', color='black', )
			plt.savefig('qfr_1-' + query_number + '_e_' + '.png')
			# plt.show()
			plt.clf()

# using PI instead of E
def qfr_2():
	
	img = mpimg.imread('small_chick.png')

	# for i in range(1, 100):

	magic_number = math.pi
	query_number = ''
	query_number_list = range(123,456)
	# query_number = str(i*math.floor(magic_number))
	candidate = ''
	
	# switch the scope of these to create buildup images
	# list_of_numbers = []
	# list_of_markers = []

	for qn in query_number_list:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

		if len(list_of_numbers) > 0:
			chart_setup()
			plt.scatter(list_of_numbers, list_of_markers, marker='.', color='black', )
			plt.savefig('qfr_1-' + query_number + '_pi_' + '.png')
			# plt.show()
			plt.clf()

def qfr_3():
	
	magic_number = math.e
	query_number = ''
	query_number_list = range(98,120)
	# query_number = str(i*math.floor(magic_number))
	candidate = ''
	
	# switch the scope of these to create buildup images
	# list_of_numbers = []
	# list_of_markers = []

	for qn in query_number_list:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

		if len(list_of_numbers) > 0:
			chart_setup()
			plt.scatter(list_of_numbers, list_of_markers, marker='.', color='black', )
			plt.savefig('qfr_1-' + query_number + '_' + str(magic_number) + '.png')
			# plt.show()
			plt.clf()

def qfr_4():

	magic_number = math.e
	query_number = ''
	query_number_list1 = range(100,150)
	query_number_list2 = range(99,149)
	# query_number = str(i*math.floor(magic_number))
	candidate = ''
	
	# switch the scope of these to create buildup images
	# list_of_numbers = []
	# list_of_markers = []

	chart_setup()
	
	for qn in query_number_list1:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	if len(list_of_numbers) > 0:
		plt.scatter(list_of_numbers, list_of_markers, marker='+', color='black', )
		
	# next
	for qn in query_number_list2:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	if len(list_of_numbers) > 0:
		plt.scatter(list_of_numbers, list_of_markers, marker='+', color='red', )
		



	import time
	s = str(time.time())
	plt.savefig('qfr_4-' + s + '.png')
	# plt.show()
	plt.clf()

def qfr_6():

	magic_number = math.e
	query_number = ''
	query_number_list1 = range(0,50, 3)
	query_number_list2 = range(0,50, 11)
	query_number_list3 = range(0,50, 17)
	# query_number = str(i*math.floor(magic_number))
	candidate = ''
	
	# switch the scope of these to create buildup images
	# list_of_numbers = []
	# list_of_markers = []

	chart_setup()
	
	for qn in query_number_list1:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	if len(list_of_numbers) > 0:
		plt.scatter(list_of_numbers, list_of_markers, marker='+', color='blue', alpha='.5')
		
	# next
	for qn in query_number_list2:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	if len(list_of_numbers) > 0:
		plt.scatter(list_of_numbers, list_of_markers, marker='+', color='red', alpha='.5')
		

	# next
	for qn in query_number_list3:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	if len(list_of_numbers) > 0:
		plt.scatter(list_of_numbers, list_of_markers, marker='+', color='green', alpha='.5')
		
		


	import time
	s = str(time.time())
	plt.savefig('qfr_6-' + s + '.png')
	# plt.show()
	plt.clf()

def qfr_7():

	magic_number = math.e
	query_number = ''
	query_number_list1 = range(0,50, 13)
	query_number_list2 = range(0,50, 273)
	query_number_list3 = range(0,50, 47)
	# query_number = str(i*math.floor(magic_number))
	candidate = ''
	
	# switch the scope of these to create buildup images
	# list_of_numbers = []
	# list_of_markers = []

	chart_setup()
	
	for qn in query_number_list1:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	if len(list_of_numbers) > 0:
		plt.scatter(list_of_numbers, list_of_markers, marker='+', color='blue', alpha='.5')
		
	# next
	for qn in query_number_list2:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	if len(list_of_numbers) > 0:
		plt.scatter(list_of_numbers, list_of_markers, marker='+', color='yellow', alpha='.5')
		

	# next
	for qn in query_number_list3:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	if len(list_of_numbers) > 0:
		plt.scatter(list_of_numbers, list_of_markers, marker='+', color='green', alpha='.5')
		
		


	import time
	s = str(time.time())
	plt.savefig('qfr_6-' + s + '.png')
	# plt.show()
	plt.clf()

def qfr_8():

	magic_number = math.e
	query_number = ''
	query_number_list1 = range(0,50, 47)
	query_number_list2 = range(0,50, 273)
	query_number_list3 = range(0,50, 47)
	# query_number = str(i*math.floor(magic_number))
	candidate = ''
	
	# switch the scope of these to create buildup images
	# list_of_numbers = []
	# list_of_markers = []

	chart_setup()
	
	for qn in query_number_list1:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	if len(list_of_numbers) > 0:
		plt.scatter(list_of_numbers, list_of_markers, marker='+', color='black', alpha='.5')
		
	# # next
	# for qn in query_number_list2:
	# 	query_number = str(qn)
	# 	list_of_numbers = []
	# 	list_of_markers = []
		
	# 	for num in range(1, 1000):
	# 		candidate = Decimal(num/magic_number) % 1
	# 		# subcandidate = str(candidate)[2:5]

	# 		if str(candidate).find( query_number ) > -1:
	# 			# print(candidate)
	# 			list_of_numbers.append( candidate )
	# 			list_of_markers.append( num )
	# 		# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	# if len(list_of_numbers) > 0:
	# 	plt.scatter(list_of_numbers, list_of_markers, marker='+', color='yellow', alpha='.5')
		

	# # next
	# for qn in query_number_list3:
	# 	query_number = str(qn)
	# 	list_of_numbers = []
	# 	list_of_markers = []
		
	# 	for num in range(1, 1000):
	# 		candidate = Decimal(num/magic_number) % 1
	# 		# subcandidate = str(candidate)[2:5]

	# 		if str(candidate).find( query_number ) > -1:
	# 			# print(candidate)
	# 			list_of_numbers.append( candidate )
	# 			list_of_markers.append( num )
	# 		# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	# if len(list_of_numbers) > 0:
	# 	plt.scatter(list_of_numbers, list_of_markers, marker='+', color='green', alpha='.5')
		
		


	import time
	s = str(time.time())
	plt.savefig('qfr_6-' + s + '.png')
	# plt.show()
	plt.clf()

def qfr_9():

	this_function_name = inspect.currentframe().f_code.co_name
	magic_number = math.e
	query_number = ''
	query_number_list1 = range(0,50, 47)
	query_number_list2 = range(0,50, 273)
	query_number_list3 = range(0,50, 47)
	# query_number = str(i*math.floor(magic_number))
	candidate = ''
	
	# switch the scope of these to create buildup images
	# list_of_numbers = []
	# list_of_markers = []

	chart_setup()
	
	for qn in query_number_list1:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	if len(list_of_numbers) > 0:
		plt.scatter(list_of_numbers, list_of_markers, marker='+', color='black', alpha='.5')
		
	# # next
	# for qn in query_number_list2:
	# 	query_number = str(qn)
	# 	list_of_numbers = []
	# 	list_of_markers = []
		
	# 	for num in range(1, 1000):
	# 		candidate = Decimal(num/magic_number) % 1
	# 		# subcandidate = str(candidate)[2:5]

	# 		if str(candidate).find( query_number ) > -1:
	# 			# print(candidate)
	# 			list_of_numbers.append( candidate )
	# 			list_of_markers.append( num )
	# 		# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	# if len(list_of_numbers) > 0:
	# 	plt.scatter(list_of_numbers, list_of_markers, marker='+', color='yellow', alpha='.5')
		

	# # next
	# for qn in query_number_list3:
	# 	query_number = str(qn)
	# 	list_of_numbers = []
	# 	list_of_markers = []
		
	# 	for num in range(1, 1000):
	# 		candidate = Decimal(num/magic_number) % 1
	# 		# subcandidate = str(candidate)[2:5]

	# 		if str(candidate).find( query_number ) > -1:
	# 			# print(candidate)
	# 			list_of_numbers.append( candidate )
	# 			list_of_markers.append( num )
	# 		# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	# if len(list_of_numbers) > 0:
	# 	plt.scatter(list_of_numbers, list_of_markers, marker='+', color='green', alpha='.5')
		
		


	import time
	s = str(time.time())
	plt.savefig(this_function_name + '_' + s + '.png')
	# plt.show()
	plt.clf()

def qfr_10():

	this_function_name = inspect.currentframe().f_code.co_name
	magic_number = math.e
	query_number = ''
	query_number_list1 = range(0,50, 47)
	query_number_list2 = range(0,50, 7)
	query_number_list3 = range(0,50, 47)
	# query_number = str(i*math.floor(magic_number))
	candidate = ''
	
	# switch the scope of these to create buildup images
	# list_of_numbers = []
	# list_of_markers = []

	chart_setup()
	
	for qn in query_number_list1:
		query_number = str(qn)
		list_of_numbers = []
		list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1
			# subcandidate = str(candidate)[2:5]

			if str(candidate).find( query_number ) > -1:
				# print(candidate)
				list_of_numbers.append( candidate )
				list_of_markers.append( num )
			# print(str(num) + " " + str(Decimal(num/7.83) % 1))

	fig, ax = plt.subplots()

	if len(list_of_numbers) > 0:
		ax.scatter(list_of_numbers, list_of_markers, 
			marker='+', 
			color='green', 
			alpha='.5',
			label=['query=' + str(qn), 'magic=' + str(magic_number), this_function_name])

	ax.legend()
	ax.grid(True)

	s = str(time.time())
	plt.savefig(this_function_name + '_' + s + '.png')
	# plt.show()
	plt.clf()

def qfr_11():

	this_function_name = inspect.currentframe().f_code.co_name
	magic_number = math.pi
	query_number = ''
	query_number_list1 = range(0,10000,47)
	candidate = ''
	
	# switch the scope of these to create buildup images
	list_of_numbers = []
	list_of_markers = []

	chart_setup()
	
	for qn in query_number_list1:
		query_number = str(qn)
		# list_of_numbers = []
		# list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1

			if str(candidate).find( query_number ) > -1:
				list_of_numbers.append( candidate )
				list_of_markers.append( num )

	fig, ax = plt.subplots()

	if len(list_of_numbers) > 0:
		ax.scatter(list_of_numbers, list_of_markers, 
			marker='+', 
			color='green', 
			alpha='.1',
			label=query_number_list1)

	ax.legend()
	ax.grid(True)

	s = str(time.time())
	plt.title(['query=' + str(qn), 'magic=' + str(magic_number), this_function_name], fontsize=20)
	plt.savefig(this_function_name + '_' + s + '.png')
	# plt.show()
	plt.clf()

def qfr_12():

	this_function_name = inspect.currentframe().f_code.co_name
	golden = (1 + 5 ** 0.5) / 2
	magic_number = golden
	query_number = ''
	query_number_list1 = [3375,10777,1111,777]
	candidate = ''

	# switch the scope of these to create buildup images
	list_of_numbers = []
	list_of_markers = []

	chart_setup()
	
	# setup 1
	for qn in query_number_list1:
		query_number = str(qn)
		# list_of_numbers = []
		# list_of_markers = []
		
		for num in range(1, 10000):
			candidate = Decimal(num/magic_number) % 1

			if str(candidate).find( query_number ) > -1:
				list_of_numbers.append( candidate )
				list_of_markers.append( num )

	fig, ax = plt.subplots()

	if len(list_of_numbers) > 0:
		ax.scatter(list_of_numbers, list_of_markers, 
			marker='+', 
			color='green', 
			alpha='.4',
			label=query_number_list1)

	ax.legend()
	ax.grid(True)

	s = str(time.time())
	plt.title(['magic=' + str(magic_number), this_function_name], fontsize=20)
	plt.savefig(this_function_name + '_' + s + '.png')
	# plt.show()
	plt.clf()

	list_of_numbers = []
	list_of_markers = []
	magic_number = math.pi

	# setup 2
	for qn in query_number_list1:
		query_number = str(qn)
		# list_of_numbers = []
		# list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1

			if str(candidate).find( query_number ) > -1:
				list_of_numbers.append( candidate )
				list_of_markers.append( num )

	fig, ax = plt.subplots()

	if len(list_of_numbers) > 0:
		ax.scatter(list_of_numbers, list_of_markers, 
			marker='+', 
			color='red', 
			alpha='.4',
			label=query_number_list1)

	ax.legend()
	ax.grid(True)

	s = str(time.time())
	plt.title(['magic=' + str(magic_number), this_function_name], fontsize=20)
	plt.savefig(this_function_name + '_' + s + '.png')
	# plt.show()
	plt.clf()

	list_of_numbers = []
	list_of_markers = []
	magic_number = math.e

	# setup 2
	for qn in query_number_list1:
		query_number = str(qn)
		# list_of_numbers = []
		# list_of_markers = []
		
		for num in range(1, 1000):
			candidate = Decimal(num/magic_number) % 1

			if str(candidate).find( query_number ) > -1:
				list_of_numbers.append( candidate )
				list_of_markers.append( num )

	fig, ax = plt.subplots()

	if len(list_of_numbers) > 0:
		ax.scatter(list_of_numbers, list_of_markers, 
			marker='+', 
			color='blue', 
			alpha='.4',
			label=query_number_list1)

	ax.legend()
	ax.grid(True)

	s = str(time.time())
	plt.title(['magic=' + str(magic_number), this_function_name], fontsize=20)
	plt.savefig(this_function_name + '_' + s + '.png')
	# plt.show()
	plt.clf()

qfr_12()

# twoseventysevenonethree_divider_algorithm()
# twoseventyseven_divider_algorithm()
# fourthirtytwo_divider_algorithm()
# schuman_divider_algorithm()
# simple_scatter()
# show_sine()
# quadratic_1()
