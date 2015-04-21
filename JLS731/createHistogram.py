'''
Created by: Joseph Song (JLS731)
Created on: 4/19/2015
Assignment 9
Description: Takes the cleaned data and sets up the bar chart data.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Suppressing warning
pd.options.mode.chained_assignment = None  # default='warn'

def setchartdata(dataset, region = 'NYC'):
    '''This is the function to reshape the data to use in the bar chart'''
    
    region = region.upper()
    
    #Allows for borough analysis
    if region != 'NYC':
        dataset = dataset[dataset.BORO == region]

    #Retrieves the year from the date
    dataset['YEAR'] = dataset['GRADE DATE'].dt.year

    #Creates new dataframe with only the necessary data
    newdataset = dataset[['GRADE', 'YEAR']]
    dflength = len(newdataset['GRADE'])
    newdataset['COUNT'] = pd.Series(np.ones(dflength))

    #Aggregates the grades
    collapseddataset = newdataset.groupby(['GRADE', 'YEAR']).sum()
    collapseddataset = collapseddataset.reset_index()

    #Reshapes the data
    dataforchart = collapseddataset.pivot(index='YEAR', columns='GRADE', values='COUNT')
    return dataforchart

def createbarchart(dataset, region = 'NYC'):
    '''This function takes in setchartdata function and plots the bar chart'''

    chartdata = setchartdata(dataset, region)

    #Plot and save charts
    chartdata.plot(kind='bar')
    plt.xlabel('Year')
    plt.ylabel('Count')
    region = region.upper()
    plt.title(region + ' Restaurant Grades Through Time')
    filename = 'grade_improvement_' + region + '.pdf'
    plt.savefig(filename)

    
