'''
Created by: Joseph Song (JLS731)
Created on: 4/18/2015
Assignment 9
Description: This is the main program to run assignment #9.
It creates the out in question 4 and the six graphs in question 5.
Since there is no user input, there is no try/except tests.
Also, I decided to not catch any exceptions since the programming is 'static'.
'''

#Load the functions and classes
from loaddata import loadcsvdata
from errorExceptions import *
from test_grades import *
from createHistogram import *
from cleandataset import *

if __name__ == '__main__':

    #Set variable list to extract from csv file
    variable_list = ['CAMIS', 'BORO', 'INSPECTION DATE', 'SCORE', 'GRADE', 'GRADE DATE', 'INSPECTION TYPE']

    rawdata = loadcsvdata('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', variable_list)
    
    print('Loading and cleaning data...')
    
    restaurantdata = cleandataset(rawdata, 'Grade')
    cleanedrestaurantdata = restaurantdata.cleandata()

    print('Testing if restaurants improved...this is going to take a while (~10 mins) go for a drink...')
    testrestaurantimprovement = test_restaurant_grades(cleanedrestaurantdata, 'CAMIS')

    #All of NYC
    testrestaurantimprovement_nyc = sum_restaurant_grades(testrestaurantimprovement, 'CAMIS', region = False)
    #By Borough
    testrestaurantimprovement_boro = sum_restaurant_grades(testrestaurantimprovement, 'CAMIS', region = True)    

    #Create plots
    NYC_plot = createbarchart(cleanedrestaurantdata, 'NYC')
    BRONX_plot = createbarchart(cleanedrestaurantdata, 'BRONX')
    BROOKLYN_plot = createbarchart(cleanedrestaurantdata, 'BROOKLYN')
    MANHATTAN_plot = createbarchart(cleanedrestaurantdata, 'MANHATTAN')
    QUEENS_plot = createbarchart(cleanedrestaurantdata, 'QUEENS')
    STATENISLAND_plot = createbarchart(cleanedrestaurantdata, 'STATEN ISLAND')


    #Create Score Analysis
    restaurantdata = cleandataset(rawdata, 'SCORE')
    cleanedrestaurantdata = restaurantdata.cleandata()

    outputrestaurantscores = create_restaurant_scores(cleanedrestaurantdata, 'CAMIS')

    print('Program complete...Goodbye')
    
