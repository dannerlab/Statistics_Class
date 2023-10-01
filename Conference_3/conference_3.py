from scipy.stats import skewnorm
from scipy.stats import shapiro
from scipy.stats import f_oneway
from scipy.stats import tukey_hsd
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
### Question 1
### Below sets up a one way Anova for the dopaamine question

residuals_shap=0.0
residuals_k=0.0
one_way_p_value=0.9
first_tukey_pair=0.0
second_tukey_pair=0.9
third_tukey_pair=0.0

while residuals_shap<=0.05 or residuals_k<=0.05 or one_way_p_value>=0.05 or first_tukey_pair<=0.05 or second_tukey_pair>=0.05 or third_tukey_pair<=0.05:

    ###Below generates the data and makes it into one array
    control_water_maze=np.random.normal(loc=75.0, scale=5.0, size=20)
    one_nM_water_maze=np.random.normal(loc=75.0, scale=5.0, size=20)
    ten_nM_water_maze=np.random.normal(loc=40.0, scale=5.0, size=20)
    twenty_nM_water_maze=np.random.normal(loc=40.0, scale=5.0, size=20)
    combined_times=np.append(control_water_maze,one_nM_water_maze)
    combined_times=np.append(combined_times,ten_nM_water_maze)
    combined_times=np.append(combined_times,twenty_nM_water_maze)
    ###Below tests the residuals for normality
    control_residual=(control_water_maze-np.mean(control_water_maze))
    one_nM_residual=(one_nM_water_maze-np.mean(one_nM_water_maze))
    ten_nM_residual=(ten_nM_water_maze-np.mean(ten_nM_water_maze))
    twenty_nM_residual=(twenty_nM_water_maze-np.mean(twenty_nM_water_maze))
    combined_residuals=np.append(control_residual,one_nM_residual)
    combined_residuals=np.append(combined_residuals,ten_nM_residual)
    combined_residuals=np.append(combined_residuals,twenty_nM_residual)
    standardized_residuals=combined_residuals/np.std(combined_residuals)
    residuals_shap=shapiro(standardized_residuals)[1]
    residuals_k=stats.kstest(standardized_residuals, 'norm')[1]
    #residuals_k=[stats.kstest(control_residual, 'norm')[1],stats.kstest(one_nM_residual, 'norm')[1],stats.kstest(ten_nM_residual, 'norm')[1],stats.kstest(twenty_nM_residual, 'norm')[1]]
    #print(residuals_shap)
    #print('K',residuals_k)
    ###Below tests the data for homogeneity of variance
    one_way_p_value=f_oneway(control_water_maze, one_nM_water_maze, ten_nM_water_maze, twenty_nM_water_maze)[1]
    ###Below runs the tukey test
    tukey_results=tukey_hsd(control_water_maze, one_nM_water_maze, ten_nM_water_maze, twenty_nM_water_maze)
    first_tukey_pair=tukey_results.pvalue[0,1]
    second_tukey_pair=tukey_results.pvalue[0,2]
    third_tukey_pair=tukey_results.pvalue[2,3]
    print(tukey_results)

col1 = "Dose:"
col2 = 'Time (s)'
doses=['Control']*len(control_water_maze)+['1 nM']*len(one_nM_water_maze)+['10 nM']*len(ten_nM_water_maze)+['20 nM']*len(twenty_nM_water_maze)

question_1 = pd.DataFrame({col1:doses,col2:combined_times})

### Question 2
### Below sets up a two way Anova for the interaction of adhd medication and sex on depression levels
