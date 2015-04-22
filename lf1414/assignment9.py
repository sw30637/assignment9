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

import functions as f

#Since file was too big for GitHub's limit, I zipped itt and now this portion unzips it
import zipfile

if __name__ == '__main__':

	fh = open('DOHMH_New_York_City_Restaurant_Inspection_Results.zip', 'rb')
	z = zipfile.ZipFile(fh)
	z.extractall()

	df = f.loaddata()	
	f.print_sum_grades(df)
	f.plot_to_pdf(df)

## Unit Tests ##

# print df
# print test_grades(['A', 'B', 'C', 'C'])
# print test_restaurant_grades(30075445)
# print truncate_by_boro('QUEENS', df)
# print sum_test_grades('QUEENS', df)