import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import csv
import sys
import testgrade
from testgrade import test_grades,test_restaurant_grades,test_nyc_restaurant_grades
from assessgrade import assessgrade


	
if __name__ == '__main__':
	try:
		Borolist = ['MANHATTAN','BROOKLYN','QUEENS','BRONX','STATEN ISLAND']
		ag = assessgrade()
		ag.calculate_grade_nyc()
		for ele in Borolist:
			ag.calculate_boro_grade(ele)
			print ele + "'s restaurants grade is " + str(ag.test_Borough_restaurant_grade(ele))+'.'
		print 'NYC restaurants grade is '+ str(test_nyc_restaurant_grades())
		print 'Now  please check graphs in the folder.'
	except: 
		KeyboardInterrupt
		print ("You have touch the KeyboardInterrupt, now the processing will stop")
		sys.exit()
