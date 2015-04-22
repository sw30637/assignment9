'''
Created on Apr 20, 2015

@author: ds-ga-1007
'''
import matplotlib.pyplot as plt

class graphNYCData():
    def __init__(self, grades):
        self.grades = grades
    
    def graph(self):
        plt.hist(self.grades)
        plt.title("NYC Restaurant Inspection Grades")
        plt.xlabel("Grades")
        plt.ylabel("Number of Restaurants")
        plt.savefig("grade_improvement_nyc.pdf")
        plt.clf()
        print "saving 'grade_improvement_nyc.pdf'\n"
        
class graphBOROData():
    def __init__(self, grades, boro):
        self.grades = grades
        self.boro = boro
        
    def graph(self):
        plt.hist(self.grades)
        plt.title(str(self.boro) + " Restaurant Inspection Grades")
        plt.xlabel("Grades")
        plt.ylabel("Number of Restaurants")
        plt.savefig("grade_improvement_" + str(self.boro) + ".pdf")
        plt.clf()
        print "saving 'grade_improvement_" + str(self.boro) + ".pdf\n"
'''
    def graphNYC(self):
        gradeCount = self.df.groupby('GRADE')['CAMIS'].nunique()
        gradeCount.plot(kind = 'bar')
        plt.title("NYC Restaurant Inspection Grades")
        plt.xlabel("Grades")
        plt.ylabel("Number of Restaurants")
        plt.savefig("grade_improvement_nyc.pdf")
        plt.clf()
    
    def graphBoro(self):
        grouped = self.df.groupby('BORO')
        
        for k,group in grouped:
            if k != 'Missing':
                gradeCount = group.groupby('GRADE')['CAMIS'].nunique()
                gradeCount.plot(kind = 'bar')
                plt.title(str(k) + " Restaurant Inspection Grades")
                plt.xlabel("Grades")
                plt.ylabel("Number of Restaurants")
                plt.savefig("grade_improvement_" + str(k).lower() + ".pdf")
                plt.clf()
'''