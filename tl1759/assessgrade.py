
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import datetime
import time
import matplotlib.dates
from testgrade import test_grades,test_restaurant_grades,test_nyc_restaurant_grades

class assessgrade():
	"""this class is to assess the grade and draw  grade graphs"""

	rawdata = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results_raw.csv", low_memory = False)
	cleaningdata1 = rawdata.dropna(subset = ['GRADE']) # get the NAN eliminated
	cleaningdata2 = cleaningdata1.query('GRADE != "Not Yet Graded"') #get the "Not Yet Graded" eliminated
	####convert  'GRADE DATE' to datetime
	cleaningdata2 = cleaningdata2.dropna(subset = ['GRADE DATE'])### remember to drop nan!!!!
	cleaningdata2['GRADE DATE'] = pd.to_datetime(cleaningdata2['GRADE DATE'],format = '%m/%d/%Y')
	###convert datetime to date use date() method
	cleaningdata2['GRADE DATE'] = [time.date() for time in cleaningdata2['GRADE DATE']]
	###sort the dataframe use time 
	cleandata = cleaningdata2.sort(['GRADE DATE'])
	gradearray = (cleandata['GRADE']).unique()
	gradelist = []
	for grade in gradearray:
		gradelist.append(grade)
	gradelist.sort()

	def test_Borough_restaurant_grade(self,Borough):
		"""this is the method to calculate each borough's restaurants GRADE"""
	
		cleandata = self.cleandata
		boromask = cleandata['BORO'] == Borough ##create a mask for each bogrough
		data = cleandata[boromask] ##use the mask to get each borough's data
		boro_camisarray = data.CAMIS.unique() ###get the unique CAMIS_ID
		boro_tempList = []
		for i in range(len(boro_camisarray)):
			this_id = boro_camisarray[i]
			n = test_restaurant_grades(this_id)
			boro_tempList.append(n)
		return sum(boro_tempList)


	def calculate_grade_nyc(self):
		cleandata = self.cleandata
		datearray = (cleandata['GRADE DATE']).unique()
		
		gradelist = self.gradelist
		nycdata = pd.DataFrame()
		for grade in gradelist:
			date_grade = {}
			for date in datearray:
				datemask = cleandata['GRADE DATE']== date#####use mask to get the date index 
				dateDF1 = cleandata[datemask] ##get the date dataFrame
				# dateDF2 = dateDF1.query('dateDF1[GRADE DATE] !="255/255/1"') #### i WANT TO USE QUERY TO DEL UNVALID DATE
				grademask = dateDF1['GRADE'] == grade####get the grade mask 
				gradeDF = dateDF1[grademask] ###get the dataframe just contain one date and a sum grade number
				date_grade[date] = len(gradeDF)
			nycdata['date'] = date_grade.keys()####add date as a column in DataFrame:data
			nycdata = nycdata.set_index(pd.DatetimeIndex(nycdata['date']))#####set the index as DatetimeIndex
			del nycdata['date'] ##del the column
			nycdata[grade] = date_grade.values() ###add grade_numbers as a new column in the DataFrame: data
			del date_grade,dateDF1,datemask,grademask ###release all the argument for reuse
		nycdata = nycdata.groupby([pd.TimeGrouper('M')]).sum() ###group by ##TiimeGrouper##to get monthly data

		nycdata.plot()
		printtitle = 'grade_improvement_'+'nyc'
		plt.title(printtitle)
		plt.savefig(printtitle+'.pdf')
		plt.show(block = False)
		return None





	def calculate_boro_grade(self,Borough):
	
		"""this is the method to show one borough with different grades"""
		cleandata = self.cleandata
		gradelist = self.gradelist
	
		datearray = (cleandata['GRADE DATE']).unique()
		data = pd.DataFrame()
		for grade in gradelist:
			boro_date_grade = {}
			grademask = cleandata['GRADE'] == grade
			cleangradedata = cleandata[grademask]
			for date in datearray:

				datemask = cleangradedata['GRADE DATE']== date#####use mask to get the date index 
				dateDF1 = cleangradedata[datemask]
				boromask = dateDF1['BORO'] == Borough####get the boro mask 
				boroDF = dateDF1[boromask]  ###get boro data
				boro_date_grade[date] = len(boroDF) ##this dictionary contains date : grade_number(sum)
	
			data['date'] = boro_date_grade.keys()####add date as a column in DataFrame:data
			data = data.set_index(pd.DatetimeIndex(data['date']))#####set the index as DatetimeIndex
			del data['date'] ##del the column
			data[grade] = boro_date_grade.values() ###add grade_numbers as a new column in the DataFrame: data
			del boro_date_grade,boroDF,dateDF1,boromask,datemask,grademask,cleangradedata ###release all the argument for reuse
		data = data.groupby([pd.TimeGrouper('M')]).sum() ###group by ##TiimeGrouper##to get monthly data

		data.plot()
		printtitle = 'grade_improvement_'+Borough.lower()
		plt.title(printtitle)
		plt.savefig(printtitle+'.pdf')
		plt.show(block = False)
		return None


