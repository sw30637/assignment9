# Name: 	graphs.py
# Author: 	Denis Stukal
# Date: 	April 18, 2015
# Summary:	
########################################################################################## 

import matplotlib.pyplot as plt
import assignment9Modules.assignment9Exceptions as ex
import assignment9Modules.selectBorough as sb
import pandas as p

class Graphs:
    '''
    Initializes a class object with 1 attribute -- self.region (NYC or one of its boroughs)
    Defines 2 functions:
                         plotGradeCountOverTime() to plot a graph for self.region
                         savePlot() to save the plot made with plotGradeCountOverTime()
    '''
    
    def __init__(self):
        '''
        Initializes a class object prompting the user for selecting a region. 
        Throws: 	urgentProgramExit exception if the user wants to exit the program
                    graphInstantiationException if KeyboardInterrupt error happens. 
        '''
        try:
            self.region = raw_input("\nType nyc if you want a graph for the whole city\nType manhattan if you want a graph for Manhattan\nType brooklyn if you want a graph for Brooklyn\nType queens if you want a graph for Queens\nType staten if you want a graph for Staten Island\nType bronx if you want a graph for Bronx\nType stop to EXIT the program\n")
            
            if self.region == 'stop':
                raise ex.urgentProgramExit()
        
        except KeyboardInterrupt:
            raise ex.graphInstantiationException()


    def plotGradeCountOverTime(self, data):
        '''
        Uses selectBorough() from assignment9Modules.selectBorough module to select data, given self.region
        Throws noSuchBoroughException if user's input does not correspond to any borough or NYC in general. 
        Aggregates data to count different grades and produces the corresponding plot plot. 
        '''
        if self.region == 'nyc':
            currentData = sb.selectBorough(data)
        elif self.region == 'manhattan':
            currentData = sb.selectBorough(data,'MANHATTAN')
        elif self.region == 'brooklyn':
            currentData = sb.selectBorough(data,'BROOKLYN')
        elif self.region == 'queens':
            currentData = sb.selectBorough(data,'QUEENS')
        elif self.region == 'staten':
            currentData = sb.selectBorough(data,'STATEN ISLAND')
        elif self.region == 'bronx':
            currentData = sb.selectBorough(data,'BRONX')
        else:
            raise ex.noSuchBoroughException()
        
        # Aggregates data by grade and date and reshapes the data. 
        gradeCounts = currentData.groupby(['GRADE', 'GRADE DATE']).agg(len)
        gradeCounts = gradeCounts['CAMIS'].unstack().transpose()
        # Transforms the date stamp into valid datetime type
        gradeCounts['new_date'] = p.to_datetime(gradeCounts.index)
        # Sorts data by date and drops dates where not all grades are present
        gradeCounts = gradeCounts.sort(columns = 'new_date').dropna()
        
        # Creates a time-series graph and makes it look good
        newFigure = plt.figure()
        newAxis = newFigure.add_subplot(1,1,1)
        outputGraph = gradeCounts.plot(ax = newAxis)
        plt.xticks(rotation = 30)
        outputGraph.tick_params(labelsize=10)
        plt.show()
        
        return newFigure
       
      
        
    def savePlot(self, plot):
        '''
        Saves the graph produced before by plotGradeCountOverTime().
        '''
        try:
            path = 'grade_improvement_%s.pdf' % self.region
            plot.savefig(path)
        except IOError:
            print 'Error in savePlot(): invalid path to a file. '
        except NameError:
            print 'Error in savePlot(): 2nd argument must be a string'
        except AttributeError:
            print 'Error in savePlot(): 1st argument must be a matplotlib figure object'
        except:
            print 'Ooops! Something wrong in savePlot() happened...'

