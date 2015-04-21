# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  assignment9.py
#  April 19,2015
#
#  Restaurant Analysis
#  It will show the cumulative rating to see if the quality of restaurants is improving. 
#
###################################


import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotter import plotterClass
  

def sourceReader(thisfile):
    '''
    Read a csv and return a dataframe after reindexing 
    '''
    restList = pd.read_csv(thisfile,  usecols=["CAMIS", "DBA", "BORO", "INSPECTION DATE", "GRADE"]).dropna()
    restList = restList[restList["GRADE"] !="Not Yet Graded"]    #clean/remove 
    restList = restList[restList["BORO"] !="Missing"]          #clean/remove 
    restList = restList.sort_index(by=["INSPECTION DATE"], ascending=[True])
    restList.index =  xrange(len(restList))       #reindex because of removed rows
    return restList


def test_grades(grade_list):
    '''
    Takes a list of grades 
    returns 
    1 if the grades are improving, ­
    - 1 if they are declining, 
    or 0 if they have stayed the same
    When A and B are compared, A is smaller than B because of numeric value of a character
    according to ASCII table. A is 65 B is 66
    
    Rating will be accumulated over time, and returned 
    '''
    rating = 0
    for item in xrange(len(grade_list)-1):
        if grade_list[item]== grade_list[item+1]:  #A, A
            rating += 0         
        elif grade_list[item]> grade_list[item+1]:     #B (66) , A (65)
            rating += 1          
        else:       #A, B
            rating += -1         
    return rating


def test_restaurant_grades(camis_id, thisList):
    '''
    calls test_grade function if CAMIS is not empty
    It will return the accumulated rating and camis_id.  
    '''
    if restList[restList["CAMIS"]==camis_id].empty:    
            print "The Camis ID does not exist"
    else:
            return camis_id, test_grades(thisList)
          


def joinRestWithRating(restList):
 '''
 This function will return a dictionary--> key:Camis | value: a list of grade
 '''
 restaurantWithRating={}
 for name, group in restList["GRADE"].groupby(restList["CAMIS"]):
     thisList = list(group)
     name, improvement = test_restaurant_grades(name, thisList)    #values are returned from test_restaurant_grade function
     restaurantWithRating[name]=improvement                        #the values will be inserted into a dictionary. 
 return restaurantWithRating


def groupRestaurant(restaurantWithRating):
    '''
    Group the restaurants by borough and the ratings for each borough will be added into a dictionary
    '''
    boroughAndImprovement={}
    for key, value in restaurantWithRating.items():
        borough = restList[restList["CAMIS"]==key]["BORO"].iloc[0]   #get the borough   
        if borough in boroughAndImprovement:
            boroughAndImprovement[borough].append(value)
        else:
            boroughAndImprovement[borough]=[]    #will create 5 keys.  e.g Manhattan, Brooklyn
            boroughAndImprovement[borough].append(value)
    return boroughAndImprovement
    
    
    
if __name__ == "__main__":
 thisfile ="DOHMH_New_York_City_Restaurant_Inspection_Results.csv"   
        #Due to the size of the file, I am not attaching the file to the github.
                                
 restList = sourceReader(thisfile)
 
 restaurantWithRating = joinRestWithRating(restList)    
 restaurantGrouped = groupRestaurant(restaurantWithRating)

 plotly =plotterClass(restaurantGrouped)
 plotly.plotBoroughs()
 
 plotlyAll =plotterClass(restaurantWithRating)
 plotlyAll.plotNYC()
 
 

     

    
    
    
    
    