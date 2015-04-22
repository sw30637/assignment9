# Name: 	assignment9.py
# Author: 	Denis Stukal
# Date: 	April 18, 2015
# Summary:	It's the main program for assignment 9 that loads restaurant data, 
# 			computes sums of restaurants' performance values and makes time plots for different grades
#
#			NB! It takes 5 minutes to print out performance values to NYC and its boroughs. Be patient!
######################################################################################################## 

import assignment9Modules.dataModule.data as dat
import assignment9Modules.gradesCheck as go
import assignment9Modules.graphsModule.graphs as g
import assignment9Modules.assignment9Exceptions as ex
import sys

if __name__ == '__main__':
    # Load and clean the data using data class from dataModule
    myDataObject = dat.RestaurantData()
    myDataObject.loadRestaurantData()
    myDataObject.cleanRestaurantData()
    
    # Sum of the function over all restaurants in a given borough
    for borough in ['MANHATTAN', 'BROOKLYN', 'BRONX', 'QUEENS', 'STATEN ISLAND']:
        print "The sum of restaurants' performance values in %s is %d" % (borough, myDataObject.boroughRestaurantGradesSum(borough))

    # Sum of the function over all restaurants in NYC
    print "The sum of restaurants' performance values across NYC is %d" % myDataObject.nycRestaurantGradesSum()


    # Prompt the user for selecting a borough (or NYC) and make graphs 
    while True:
        try:
            # Instantiate a Graphs class object, make and save a graph
            graphObject = g.Graphs()
            graph = graphObject.plotGradeCountOverTime(myDataObject.data)
            graphObject.savePlot(graph)
        
            userInput = raw_input('\nDo you want to exit? Type y for yes, n for no\n')
            if userInput == 'y':
                break
            elif userInput != 'n':
                print 'Illegal input -- program continues'
        except KeyboardInterrupt:
            print 'You typed ^C -- exiting the program..'
            sys.exit(1)
        except ex.noSuchRestaurantException:
            print ex.noSuchRestaurantException()
            continue
        except ex.noSuchBoroughException:
            print ex.noSuchBoroughException()
            continue
        except ex.noSuchDataException:
            print ex.noSuchDataException()
            sys.exit(1)
        except ex.loadedDataException:
            print ex.loadedDataException()
            sys.exit(1)
        except ex.graphInstantiationException:
            print ex.graphInstantiationException()
            continue
        except ex.urgentProgramExit:
            print ex.urgentProgramExit()
            sys.exit(0)
