'''
Created by: Joseph Song (JLS731)
Created on: 4/10/2015
Assignment 9
Description: Loads in a csv file and returns a DataFrame dataset.
Note: this function was taken from the previous assignment and modified for assignment 9. 
'''

import pandas as pd

def loadcsvdata(filename, variables=''):
    ''' Loads csv file and returns a DataFrame. Takes in a variable list to use to extract specific columns.'''
    if variables =='':
        data = pd.read_csv(filename)
    else:
        data = pd.read_csv(filename,usecols = variables)

    data['GRADE DATE'] = pd.to_datetime(data['GRADE DATE'])
    data['INSPECTION DATE'] = pd.to_datetime(data['INSPECTION DATE'])
    return data


