'''
For each restaurant we examine if the grade improves, declines, or stays the same over time, 
using the function created earlier in assignment 9.

Created on Apr 14, 2015
@author: Adam Biesenbach
'''

import numpy as np 

def GradeAllNYC(CleanGrades):
    """ Generate the summed grade trend measures for all NYC."""
   
    Grouped = CleanGrades[['CAMIS', 'GRADE', 'INSPECTION DATE']].groupby(CleanGrades['CAMIS'])

    # Generate a dictionary for the CAMIS IDs and their improvement identifiers.
    
    GradeResults = {}
    for camis_id, group in Grouped:
        
        GradeResults.update({camis_id: test_restaurant_grades(group, camis_id)})
    
    print "Here is the summed grade for all NYC: " + str(sum(GradeResults.values()))
    
def GradeByBoro(CleanGrades):
    """ Generate the summed grade trend measures by Borough."""
   
    # Initialize an empty dictionary to fill out with our results.
    BoroGrade = {} 
    
    # Look over the Boroughs in our data.
    for Boro in CleanGrades.BORO.unique():
        
        # Initialize the grade to zero for each Borough.
        Grade = 0
        BoroData = CleanGrades[(CleanGrades.BORO == Boro)]
        for camis in BoroData.CAMIS.unique():
            Grade += test_restaurant_grades(BoroData,camis)
            BoroGrade[Boro] = Grade
            
    print "Here is the summed grade for the 5 Boroughs: " 
    print BoroGrade
    
def test_restaurant_grades(CleanGrades, camis_id):
    """ for each restaurant, this function will 
    attempt to determine whether or not the restaurants grade
    is improving over time. """
    
    # Select only the CAMIS ID we're interested in.
    CleanGrades = CleanGrades[CleanGrades['CAMIS']==camis_id]
    
    # Put the DF to a list, so we can use the test_grades function. 
    GradeList =CleanGrades['GRADE'].tolist()    
    return test_grades(GradeList)

def test_grades(GradeList):
    """ A function that takes a list of grades sorted in date order and 
        returns 1 if the grades are improving., -1 if they are declining,
        or zero if they have stayed the same. """
    
    #For those who were graded only once, set the measurement to zero. 
    if len(GradeList) == 1:
        return 0
   
    else:
        
        # Reassign letter grades to numbers.
        GradeList =  QuantifyGrades(GradeList)
        
        # If there are only two grades, it's easy to compute the right number.
        if len(GradeList) == 2:

            if GradeList[1] - GradeList[0] > 0:
                return 1
            elif  GradeList[1] - GradeList[0] < 0:
                return -1
            else:
                return 0
        
        else:
            
            # Our method our determining if the grades are increasing is fitting the data with a linear
            # regression model. Use the Beta (slope) coefficient to create the measurement. 
            # If the beta is positive, assign a grade of 1, negative -1, and zero 0. 
            
            x = np.arange(0,len(GradeList))
            y = np.array(GradeList)
            
            # Fit the linear model. 
            LinearModelEstimates = np.polyfit(x,y,1)
               
            # Set a tolerance for nearness to zero... otherwise we wont categorize
            # their improvement measures correctly, since some coeff's are very
            # close to zero.
             
            LinearModelEstimates[np.abs(LinearModelEstimates) < 0.0001 ] = 0
                        
            if LinearModelEstimates[0]>0:
                return 1
            elif LinearModelEstimates[0]==0:
                return 0
            else:
                return -1

def QuantifyGrades(GradeList):
    """Construct the mapping from letters to numbers."""
    
    MyGradeCoverstion = {"A": 4.0, "B": 3.0, "C": 2.0 }  
    return [MyGradeCoverstion[i] for i in GradeList]
