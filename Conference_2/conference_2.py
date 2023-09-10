from scipy.stats import skewnorm
from scipy.stats import shapiro
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.options.display.max_columns = None
#Question 1 Guiness

### Below creates data to be analyzed for independent samples t test
t_score=0.9
shap_test_1=0.05
shap_test_2=0.05
while t_score>=0.05 and shap_test_1<=0.05 and shap_test_2<=0.05:
    
    hops_1_scores=np.random.normal(loc=75.0, scale=10.0, size=25)
    hops_2_scores=np.random.normal(loc=35.0, scale=10.0, size=25)
    
    t_score=stats.ttest_ind(a=hops_1_scores, b=hops_2_scores, equal_var=True)[1]
    shap_test_1=shapiro(hops_1_scores)[1]
    shap_test_2=shapiro(hops_2_scores)[1]


col1 = "Hops A:"
col2 = 'Batch 1 Soft Resin ml'
col3 = "Hops B:"
col4 = 'Batch 2 Soft Resin ml'
sample_number=list(range(1,len(hops_1_scores)+1))

data_frame_1 = pd.DataFrame({col1:sample_number,col2:hops_1_scores,col3:sample_number,col4:hops_2_scores})

### Below creates data to be analyzed by a mann whitney u test for question 2
##The result should be that there is no difference between the groups

shap_test_1=0.9
shap_test_2=0.9
skewness = -1000
whitney_p_value=0.01  
while shap_test_1>=0.05 and shap_test_2>=0.05 and whitney_p_value<=0.05:

    neurons_1 = skewnorm.rvs(a = skewness,loc=8000, scale=500,  size=20)  #Skewnorm function
    shap_test_1=shapiro(neurons_1)[1]   #Shapiro-Wilk test for normality
    neurons_2 = skewnorm.rvs(a = skewness,loc=8000, scale=500,  size=20)  #Skewnorm function
    shap_test_2=shapiro(neurons_2)[1] 

    whitney_p_value=stats.mannwhitneyu(neurons_1,neurons_2,alternative='two-sided')[1]

col1 = "Control Measurement Number:"
col2 = 'Control Fluorescence'
col3 = "Drug Measurement Number:"
col4 = 'Drug Fluorescence'
sample_number=list(range(1,len(neurons_1)+1))

data_frame_2 = pd.DataFrame({col1:sample_number,col2:neurons_1,col3:sample_number,col4:neurons_2})

## Below creates data to be analyzed with a rank sum test for question 3
## The result should be that there is a difference between the groups
rank_p_value=0.9
shap_test_1=0.9
shap_test_2=0.9

while shap_test_1>=0.05 and shap_test_2>=0.05 and rank_p_value>=0.05:
    
    healthy_horse=stats.uniform.rvs(size=40, loc=0.8, scale=0.1)
    shap_test_1=shapiro(healthy_horse)[1]
    injured_horse=stats.uniform.rvs(size=40, loc=0.5, scale=0.1)   
    shap_test_2=shapiro(injured_horse)[1] 
    rank_p_value=stats.ranksums(healthy_horse, injured_horse)[1]

col1 = "Horse Gait Measurement Number Before:"
col2 = 'Before Race Head Nod Location in Normalized Gait Cycle'
col3 = "Horse Gait Measurement Number After:"
col4 = 'After Race Head Nod Location in Normalized Gait Cycle'
sample_number=list(range(1,len(healthy_horse)+1))

data_frame_3 = pd.DataFrame({col1:sample_number,col2:healthy_horse,col3:sample_number,col4:injured_horse})


### Below creates data to be analyzed by a paired samples t-test and there should be
### a difference between the groups
t_score=0.9
shap_test_1=0.05
shap_test_2=0.9
while t_score>=0.05 and shap_test_1<=0.05 and shap_test_2>=0.05:
    
    rat_sniffs_before=np.floor(np.random.normal(loc=25.0, scale=2.0, size=25))
    rat_sniffs_skew = np.ceil(skewnorm.rvs(a = skewness,loc=3, scale=2,  size=25))
    #rat_sniffs_after=np.random.normal(loc=10.0, scale=2.0, size=25)
    rat_sniffs_after=rat_sniffs_before+rat_sniffs_skew
    
    t_score=stats.ttest_rel(a=rat_sniffs_before, b=rat_sniffs_after)[1]
    shap_test_1=shapiro(rat_sniffs_before)[1]
    shap_test_2=shapiro(rat_sniffs_after)[1]


col1 = "Rat ID Before:"
col2 = 'Before Treatment Sniffs'
col3 = "Rat ID After:"
col4 = 'After Treatment Sniffs'
sample_number=list(range(1,len(rat_sniffs_before)+1))

data_frame_4 = pd.DataFrame({col1:sample_number,col2:rat_sniffs_before,col3:sample_number,col4:rat_sniffs_after})

with pd.ExcelWriter('conference_2_dataset.xlsx') as writer:
       
    # use to_excel function and specify the sheet_name and index
    # to store the dataframe in specified sheet
    data_frame_1.to_excel(writer, sheet_name="Question 1", index=False)
    data_frame_2.to_excel(writer, sheet_name="Question 2", index=False)
    data_frame_3.to_excel(writer, sheet_name="Question 3", index=False)
    data_frame_4.to_excel(writer, sheet_name="Question 4", index=False)