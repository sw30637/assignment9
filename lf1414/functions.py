'''
DS-1007 Programming for Data Science
Assignment 9

Lily Fung
April 20, 2015

'''

import pandas as p
import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.dates as mdates


# Loading Dataframe into Pandas #
def loaddata():
	# Reads the CSV file and translates into Data Frame
	df = p.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv')
	
	# Drops all records with missing data
	df = df.dropna()
	
	# Selects only records with grades that are A, B, or C
	df = df[df['GRADE'].isin(['A','B','C'])]
	
	# Drops all other columns that we are not using for analysis
	df = df.drop(['DBA', 'BUILDING', 'STREET', 'ZIPCODE', 'PHONE', 'CUISINE DESCRIPTION', 'INSPECTION DATE', 'ACTION', 'VIOLATION CODE', 'VIOLATION DESCRIPTION', 'CRITICAL FLAG', 'SCORE', 'RECORD DATE', 'INSPECTION TYPE'],1)

	# Clean up weird thing with first column's name
	df = df.rename(columns={'\xef\xbb\xbfCAMIS': 'CAMIS'})

	# Convert date to date-object
	df['GRADE DATE'] = p.to_datetime(df['GRADE DATE'])

	return df


# The function test_grades(grade_list) takes a list of strings with acceptable values 'A', 'B', 'C'
# and returns 1 if grades are improving, 0 if no change, and -1 if they are worsening.
# The function first turns the grades list into integers A = 3, B = 2, C = 1.
# Then it splits the list into two, and takes the average of the two lists.
# If the average of the latter half is greater than the first, then grades are improving, etc.
def test_grades(grade_list):
	grade_list_length = len(grade_list) # calculates the length of the grades list
	grades_to_value = {'A': 3, 'B': 2, 'C': 1} # a dictionary to map grades to integer values
	analysis_list = [] # the empty list that will turn string into integer list
	for grade in grade_list: # iterate through the grades list and append int accordingly
		analysis_list.append(grades_to_value[grade])
	# breaks list into 2
	if grade_list_length > 1:
		list1 = analysis_list[:grade_list_length/2] 
		list2 = analysis_list[grade_list_length/2:]

	# takes averages of the two lists
		avg_first_half = np.mean(list1)
		avg_secnd_half = np.mean(list2)
	# returns based on if second half is greater, less than, or equal to first half
		if avg_secnd_half > avg_first_half:
			return 1
		if avg_secnd_half < avg_first_half:
			return -1
		else:
			return 0
	else:
		return 0

# This function takes the camis_id and performs test_grades on the list of grades it generates.
# It generates a list of the grades that that restaurant has received, sorted by the date which that grade was received. 
def test_restaurant_grades(camis_id, data):
	df = data
	data_by_cami = df[df['CAMIS']==camis_id].sort_index(by=['GRADE DATE'], ascending=[True])
	return test_grades(data_by_cami['GRADE'])

# This function truncates the dataframe specified by all_data by borough, specified by boro.
def truncate_by_boro(boro, all_data):
	df = all_data
	if boro == 'BRONX':
		df = df[df['BORO'] == 'BRONX']

	if boro == 'BROOKLYN':
		df = df[df['BORO'] == 'BROOKLYN']

	if boro == 'MANHATTAN':
		df = df[df['BORO'] == 'MANHATTAN']

	if boro == 'QUEENS':
		df = df[df['BORO'] == 'QUEENS']

	if boro == 'STATEN ISLAND':
		df = df[df['BORO'] == 'STATEN ISLAND']
	
	else:
		df = df
	return df

# This function takes two inputs, boro and a dataframe, and performs test_restaurant_grades on all the restaurants in the area specified by the boro input. It does so by first making a subset of the data based on borough specified, then interates through the unique restaurant data to perform the test_grades on the list of grades. 
def sum_test_grades(boro, all_data):
	df = truncate_by_boro(boro, all_data)
	sum_grades = 0

	unique_camis = df['CAMIS'].unique()

	for camis_id in unique_camis:
		sum_grades += test_restaurant_grades(camis_id, df)
	
	return sum_grades

def len_boro(boro, all_data):
	df = truncate_by_boro(boro, all_data)
	unique_camis = df['CAMIS'].unique()
	return len(unique_camis)

# This function prints the results for the previously created function.
def print_sum_grades(data):
	df = data
	print "Sum of Improvement Scores Out of Total Score Possible by Borough"
	print "Bronx: ", sum_test_grades('BRONX', df), "/", len_boro('BRONX', df)
	print "Brooklyn: ",sum_test_grades('BROOKLYN', df) , "/", len_boro('BROOKLYN', df)
	print "Manhattan: ",sum_test_grades('MANHATTAN', df) , "/", len_boro('MANHATTAN', df)
	print "Queens: ",sum_test_grades('QUEENS', df) , "/", len_boro('QUEENS', df)
	print "Staten Island: ",sum_test_grades('STATEN ISLAND', df) , "/", len_boro('STATEN ISLAND', df)
	print "All Boroughs: ",sum_test_grades('ALL', df) , "/", len_boro('ALL', df)

# This function plots by year the number of times an A, B, or C was recorded.
def plot_grades(all_data, boro, file_name):
	df = truncate_by_boro(boro, all_data)
	df2 = df.groupby(['GRADE DATE', 'GRADE']).count().reset_index()
	df2_pivot = df2.pivot(index='GRADE DATE', columns='GRADE', values='CAMIS').resample('A', how='sum')
	df2_pivot.plot(kind='bar', stacked=False)

	# This sets the tickmarks appropriately, since converting from date-time to year at this point of the process is more complicated than just adjusting the tickmark names themselves. 
	if len(df2_pivot) == 5:
		plt.xticks(range(5), [2011, 2012, 2013, 2014, 2015])
	if len(df2_pivot) == 6:
		plt.xticks(range(6), [2010, 2011, 2012, 2013, 2014, 2015])

	plt.savefig(file_name)

# This function calls the plotting function and saves the plots as pdfs.
def plot_to_pdf(data):
	df = data
	plot_grades(df, 'ALL', 'grade_improvement_nyc.pdf')
	plot_grades(df, 'BRONX','grade_improvement_bronx.pdf')
	plot_grades(df, 'BROOKLYN', 'grade_improvement_brooklyn.pdf')
	plot_grades(df, 'MANHATTAN','grade_improvement_manhattan.pdf')
	plot_grades(df, 'QUEENS','grade_improvement_queens.pdf')
	plot_grades(df, 'STATEN ISLAND','grade_improvement_staten.pdf')

if __name__ == '__main__':
	df = loaddata()	
	print_sum_grades()
	plot_to_pdf()

## Unit Tests ##

# print df
# print test_grades(['A', 'B', 'C', 'C'])
# print test_restaurant_grades(30075445)
# print truncate_by_boro('QUEENS', df)
# print sum_test_grades('QUEENS', df)