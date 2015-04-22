'''
Created by: Joseph Song (JLS731)
Created on: 4/19/2015
Assignment 9
Description: These are the functions to test whether or not grades are improving.
My criteria to see if grades are improving is to take the first grade and compare it
to the last grade for each restaurant. If the grade improved score = 1, if it stayed the same,
score = 0, if grade declined, score = -1.
'''
import pandas as pd
import numpy as np



def gradevaluetable():
    '''This is a static function to create a table to the grade and the value'''
    grade = pd.Series(['A','B','C','Not Yet Graded', 'Z', 'P'])
    value = pd.Series([3,2,1,0,-1,-2])
    gradedataframe = pd.concat([grade, value], axis = 1)
    gradedataframe.columns = ['GRADE', 'GRADE VALUE']
    return gradedataframe

def test_grades(grade_list):
    ''' This is a function to compare first and last grade'''
    first = grade_list[0]
    last = grade_list[-1]
    if (first > last):
        grade = -1
    elif (first == last):
        grade = 0
    elif (first < last):
        grade = 1
    return grade

def test_score(grade_list):
    ''' This is a function to compare first and last score'''
    first = grade_list[0]
    last = grade_list[-1]
    grade = first - last
    return grade

def test_restaurant_grades(dataset, camis_id):
    '''This is a function to loop through all the restaurants'''
    dflength = len(dataset[camis_id])
    dataset['GRADE CHANGE'] = pd.Series(np.zeros(dflength))
    unique_id = dataset.groupby([camis_id])
    for name, group in unique_id:
        temp_list = dataset.loc[dataset[camis_id] == name]
        grade_list = np.array(temp_list['GRADE VALUE'])
        grade_change = test_grades(grade_list)
        dataset.ix[dataset.CAMIS==name, 'GRADE CHANGE']=grade_change
    return dataset

def sum_restaurant_grades(dataset, camis_id, region = False):
    '''This is a function to sum up the scores'''
    dataset_agg = dataset.groupby([camis_id, 'BORO']).mean()
    if region == False:
        dataset_final = dataset_agg['GRADE CHANGE'].sum()
        np.savetxt('NYC_Grade.csv', np.array(dataset_final).reshape(1,), header = 'NYC Grade Change', fmt='%5.0f')
    elif region == True:
        dataset_agg = dataset_agg.reset_index()
        dataset_final = dataset_agg.groupby('BORO').sum()
        dataset_final.to_csv('ByBorough_Grade.csv', columns = [ 'GRADE CHANGE'])
    return dataset_final

def create_restaurant_scores(dataset, camis_id):
    '''This is a function to create the change in the score for each restaurant'''

    #Retrieves the year from the date
    dataset['YEAR'] = dataset['GRADE DATE'].dt.year

    newdataset = dataset[['CAMIS', 'SCORE', 'YEAR']]
    dflength = len(dataset[camis_id])
    dataset['SCORE CHANGE'] = pd.Series(np.zeros(dflength))

    #Take the mean of the score for each year for each restaurant
    collapseddataset = newdataset.groupby([camis_id, 'YEAR']).mean()
    collapseddataset = collapseddataset.reset_index()
    unique_id = dataset.groupby([camis_id])

    #Calculate the change in the score for each restaurant
    for name, group in unique_id:
        temp_list = dataset.loc[dataset[camis_id] == name]
        score_list = np.array(temp_list['SCORE'])
        score_change = test_score(score_list)
        collapseddataset.ix[collapseddataset.CAMIS==name, 'SCORE CHANGE']=score_change
    collapsedbyCAMIS = collapseddataset.groupby([ camis_id]).mean()
    collapsedbyCAMIS.to_csv('ScoreChangeByRestaurant.csv')
    return collapsedbyCAMIS
