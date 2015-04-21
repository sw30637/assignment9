'''
Created on Apr 20, 2015

@author: ds-ga-1007
'''
import pandas as pd
from dataCleanup import *
from testRestaurantGrades import *
from fileLoading import *
from graphData import *

if __name__ == '__main__':

	grades = loadGrades()

	grades = removeNA(grades)
	cleanGrades = removeInvalidGrades(grades)

	groupedByBORO = cleanGrades.groupby('BORO')

	#set overall improvement grade in NYC to 0
	nycImprovement = []

	for k,group in groupedByBORO:
		groupedByCAMIS = group.groupby('CAMIS')

		improvement = []

		if k != 'Missing':
			print str(k) + ' improvement over time:'
			for restaurant,group in groupedByCAMIS:
				result = test_restaurant_grades(group)
				improvement.append(result)
			nycImprovement += improvement
			print sum(improvement)
			graphBORO = graphBOROData(improvement, str(k))
			graphBORO.graph()
		
	print 'NYC improvement over time:'
	print sum(nycImprovement)

	#graph NYC data
graphNYC = graphNYCData(nycImprovement)
graphNYC.graph()
