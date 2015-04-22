import pandas as pd
import matplotlib.pyplot as plt

def test_grades(grade_list):
    
    change = 0
    for i in range(len(grade_list)-1):
        if grade_list[i] < grade_list[i+1]: # A<B, means declining
            change = change -1
        elif grade_list[i] > grade_list[i+1]: # B>A, means impoving
            change = change +1
    if change >0:
        return 1
    elif change <0:
        return -1
    else:
        return 0
        

def test_restaurant_grades(camis_id):
    
    dataframe = clean_df[clean_df['CAMIS']==camis_id].sort('GRADE DATE')
    grade_list = list(dataframe['GRADE'])
    return test_grades(grade_list)
    

def get_improvement(CAMIS_list):
    improvement = 0
    for id in CAMIS_list:
        improvement = improvement + test_restaurant_grades(id)
    return improvement



def draw_graph(dataframe, filename):
    try:
        pivoted = dataframe.pivot('GRADE DATE', 'CAMIS', 'GRADE') 
        grade_counts = pivoted.apply(pd.Series.value_counts, axis=1) 
        grade_counts.plot()
        plt.savefig(filename)
        plt.close()
    except ValueError:
        pass