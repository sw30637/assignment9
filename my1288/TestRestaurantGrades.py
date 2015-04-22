####################################################################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Assignment 9
#
#	This file contains the function test_restaurant_grades(camis_id)
#	The function reads in a camis_id and then sorts the grade list according to date
#	It calls the test_grade function in order to get a performance feedback for each camis_id
#
####################################################################################################

# Import the modules needed
import pandas as pd
import numpy as np
from TestGrades import *
from datetime import datetime

def test_restaurant_grades(camis_id, dataset):

	performances = []

	# Run a for loop to get the performance for each camis_id
	for camis in camis_id:
		# Reads in each cami_ID and then cleans up the dataset according to that ID
		new_data = dataset.loc[dataset['CAMIS']==int(camis)]

		# Drop the nan values and convert to datetime to sort dataset in ascending dates
		new_data = new_data.loc[new_data['GRADE DATE'].isin(new_data['GRADE DATE'].dropna().values)]
		new_data['GRADE DATE'] = new_data['GRADE DATE'].apply(lambda x: datetime.strptime(x, '%m/%d/%Y'))
		sorted_data = new_data.sort(['GRADE DATE'])

		# Return the performance value
		#print test_grades(sorted_data['GRADE'].tolist())
		performances.append(test_grades(sorted_data['GRADE'].tolist()))

	clean_performances = [x for x in performances if x is not None]
	return clean_performances
