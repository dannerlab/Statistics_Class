from scipy.stats import skewnorm
from scipy.stats import shapiro
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numValues = 20
skewness = -1000   #Negative values are left skewed, positive values are right skewed.

shap_test=0.9
while shap_test>=0.05:
    random = skewnorm.rvs(a = skewness,loc=8000, scale=500,  size=numValues)  #Skewnorm function
    shap_test=shapiro(random)[1]   #Shapiro-Wilk test for normality

col1 = "Patient ID:"
col2 = "White Blood Count (WBC)/µL"
data_frame1 = pd.DataFrame({col1:x,col2:random})

#data.to_excel('Problem1_dataset.xlsx', sheet_name='sheet1', index=False)


#Plot histogram to check skewness
plt.hist(random,bins=4, color = 'red')
plt.show()
sample_number=list(range(1,101))
samp_average=[]
pop_shap_test=0.
count=0
while pop_shap_test<=0.2 and count <100:
    random = skewnorm.rvs(a = skewness,loc=8000, scale=500, size=numValues)
    samp_average.append(np.mean(random))
    if count>3:
        shap_test=shapiro(samp_average)[1] 
    count=count+1
plt.hist(samp_average, color = 'red')
sample_number=list(range(1,count+1))
plt.show()

col1 = "Sample Means:"
col2 = "Average White Blood Count (WBC)/µL"
data_frame2 = pd.DataFrame({col1:sample_number,col2:samp_average})



ID=['A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116']
ID2=['A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133']

t_score=0.9

while t_score>=0.05:
    student_1_scores=np.random.normal(loc=75.0, scale=10.0, size=17)
    student_2_scores=np.random.normal(loc=35.0, scale=10.0, size=17)
    t_score=stats.ttest_ind(a=student_1_scores, b=student_2_scores, equal_var=True)[1]


col1 = "Student A:"
col2 = 'Score'
col3 = "Student B:"
col4 = 'Score2'


data_frame3 = pd.DataFrame({col1:ID,col2:student_1_scores,col3:ID2,col4:student_2_scores})



with pd.ExcelWriter('Problem1_dataset.xlsx') as writer:
       
    # use to_excel function and specify the sheet_name and index
    # to store the dataframe in specified sheet
    data_frame1.to_excel(writer, sheet_name="Question 1", index=False)
    data_frame2.to_excel(writer, sheet_name="Question 1 Part B", index=False)
    data_frame3.to_excel(writer, sheet_name="Question 2", index=False)