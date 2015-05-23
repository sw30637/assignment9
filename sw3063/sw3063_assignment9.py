'''
Assignment 9
Sarah Welt
'''


import numpy as np
import sys
import json
import matplotlib.pyplot as plt
import pandas as pd

#Q2
data_frame= pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', low_memory= false)

d= data_frame[['']]


d= d[d['GRADE'].isin(['A','B','C'])]

e = d[d['GRADE'].isin(['A','B','C'])]
e['GRADE DATE'] = pd.to_datetime(e['GRADE DATE'])

#drop_duplicates

#set_index


#Q3
np.linalg.listsq

grades= [grade_dict[grade]] for grade in grade_list]

def test_grades(grade_list, reverse=False):
        """ test whether a list of grades has an increasing trend by fit a linear regression model to it """
        n = len(grade_list)
        if n == 1:
                return 0
        x = np.arange(0, 2, 2./n)
        A = np.array([x, np.ones(n)])
        grade_dict = {'A': 2, 'B': 1, 'C': 0}
        try:
                y = [grade_dict[g] for g in grade_list]
            except KeyError as e:
                    sys.exit('There should only be 3 levels of grades: A, B, or C')
                w = np.linalg.lstsq(A.T, y)[0]
    #Got the 0.375 by assuming the sequence A, B, B, B, A, A, A has an increasing trend
    if w[0] > 0.375:
            trend = 1
        elif w[0] < -0.375:
                trend = -1
            else:
                    trend = 0
                return -trend if reverse else trend
    if w[0] > 0.375:
            trend = 1
        elif w[0] < -0.375:
                trend = -1
            else:
                    trend = 0
                return -trend if reverse else trend


#return trend in reverse else trend


#Q4
'''
Do grades
create new variable

sort 'grade date'

counts y axis
date x axis

counts=[]

date= [current_date]

plot_date

legend
title
save fig
''''