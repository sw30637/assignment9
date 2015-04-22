'''
The graph functions for assignment 9. 

Created on Apr 19, 2015
@author: Adam Biesenbach
'''

import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

def  GenerateGraphs(CleanGrades):
    """Generate the graphs of the number of restaurants by grade over time for the 
    different Boroughs, plus NYC."""
    
    # Get a list of the Boroughs in our data, plus NYC.
    Areas = CleanGrades.BORO.unique()
    Areas = Areas.tolist()
    Areas.append("NYC")
    
    try:
        # For each Borough plus NYC as a whole, generate the plots. 
        for Area in Areas: 
            # Get the grade counts over time. 
            GraphData = GetGradeCountByTime(CleanGrades, Area)
            GraphData.plot(title = 'Count of Restaurant Health Grades in ' + str(Area))
            if Area == "STATEN ISLAND":
                title = 'grade_improvement_staten'
            else:
                title = 'grade_improvement_' + Area.lower()
            pp = PdfPages(title+'.pdf')
            pp.savefig()
            pp.close()
    except IOError:
        print "\n whoops...I/O error... check to make sure that the file and directory exist for the *.pdf files being created."
      
def GetGradeCountByTime(CleanData, Area):
    '''Returns a Data Frame with rows (index) as date, columns as grade rating for 
    restaurants.'''
    
    if Area == 'NYC':       
        # Reshapes data with date down the rows, CAMIS as columns, and Grades filling it out. 
        pivoted = CleanData.pivot('INSPECTION DATE', 'CAMIS', 'GRADE')
    else:    
        # Else do the same, just with the borough data.
        pivoted = CleanData[CleanData['BORO'] == Area].pivot('INSPECTION DATE', 'CAMIS', 'GRADE') 
    # Fill empties with NaNs.
    pivoted = pivoted.ffill()
    # Count across the rows. 
    GradeCounts = pivoted.apply(pd.Series.value_counts, axis=1)  
    return GradeCounts

