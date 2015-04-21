####################################################################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Assignment 9
#
#	This file contains the function test_grades
#	The function reads in an array of grades sorted according to the dates and calculates whether the grade
#	is improving or declining 
#
####################################################################################################

# Import the modules needed
from scipy.stats import mode

'''
This function comes up with an overall performance evaluation for the given grades for a restaurant
It takes in a grade list already sorted by date
It then cleans up the list and makes a nex list of grades that actually judge performance
If the grade improves from initial value to latest it will store a 1 in the performance list
If the grade declines it will contain a -1
A zero will be given if there is no change in the current and next grade
The modal value in the performance list is returned by the function to give an idea of the overall
'''
def test_grades(grade_list):

	# create an empty list which will take in only the grade letters and disgard any unwanted values
	clean_grade_list = []

	try:
		# Start a for loop to check all the values in the input array
		for grade in grade_list:

			# Put a condition which checks for letter grades
			if grade=='A' or grade=='B' or grade=='C':
				clean_grade_list.append(grade)
			# Ignore all other values
			else:
				pass

		# Set two variables to compare the current and next value in the array
		initial = clean_grade_list[0]
		latest = clean_grade_list[-1]

		# Make comparisons. If the grade decreases -1, improves 1, same 0
		# These values are appended in the array performance
		if initial < latest:
			return -1
		elif initial > latest:
			return 1
		else:
			return 0


	# Inform the user that the input array is not the correct type
	except:
		pass
