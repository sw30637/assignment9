'''
Created on Apr 20, 2015

@author: ds-ga-1007
'''
import pandas as pd

def removeNA(df):
    '''remove entries with missing data in grades'''
    grades = df.dropna(subset = ['GRADE'])
    
    return grades

def removeInvalidGrades(df):
    '''remove rows with grades not equal 'A', 'B', or 'C'''
    df['is_valid'] = (df['GRADE'] == 'A') | (df['GRADE'] == 'B') | (df['GRADE'] == 'C')
    cleanDf = df[df.is_valid != False]
    
    return cleanDf

