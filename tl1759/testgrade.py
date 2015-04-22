import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import datetime
import csv
def load_data():
	global cleandata
	rawdata = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results_raw.csv", low_memory = False)
	cleaningdata1 = rawdata.dropna(subset = ['GRADE']) # get the NAN eliminated
	cleaningdata2 = cleaningdata1.query('GRADE != "Not Yet Graded"') #get the "Not Yet Graded" eliminated
	cleaningdata2['GRADE DATE'] = pd.to_datetime(cleaningdata2['GRADE DATE'],format = '%m/%d/%Y')###convert to datetime
	

	
	cleandata = cleaningdata2.sort(['GRADE DATE'])####sort the dataframe by datetime
load_data()	
def test_grades(grade_list):
	"""this is the funciton to test grade changes"""
	i = 0
	change_list = []
	for i in range(len(grade_list)-1):
		m = ord(grade_list[i])
		n = ord(grade_list[i+1])
		if m < n:
			k = -1
		elif m == n:
			k = 0
		else:
			k = 1
		change_list.append(k)	
	return sum(change_list)

def test_restaurant_grades(camis_id):
	"""this is a function to test each restaurant grade changes"""
	gradeseries = (cleandata[cleandata.CAMIS == camis_id]).GRADE
	tempList = []
	for ele in gradeseries:
		tempList.append(ele) ###### the tempList is used to calculate each restaurant's grade
	thisrestaurant_grade = test_grades(tempList)
	return thisrestaurant_grade

def test_nyc_restaurant_grades():
	"""this is the function that gets grade of the whole city"""
	camisarray = cleandata.CAMIS.unique()# get the CAMIS_ID uniquely
	sumgrade = [] # the list that contain all restaurants' sum grade
	for i in range(len(camisarray)):

		camis_id = camisarray[i]# get  each restaurant's  CAMIS_ID
		gradeseries = (cleandata[cleandata.CAMIS == camis_id]).GRADE
		tempList = []
		for ele in gradeseries:
			tempList.append(ele) ###### the tempList is used to calculate each restaurant's grade
		k = test_grades(tempList) ### k is the sum grade of each restaurant 
	 	sumgrade.append(k) #### list sumgrade append each restaurant's grade a
	return sum(sumgrade) ###return the sum of all restaurants 



