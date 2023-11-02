from scipy.stats import skewnorm
from scipy.stats import shapiro
from scipy.stats import f_oneway
from scipy.stats import tukey_hsd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import AnovaRM
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

residuals_shap=0.0
residuals_k=0.0
one_way_p_value=0.9
first_tukey_pair=0.0
second_tukey_pair=0.9
third_tukey_pair=0.0
two_anova_p1=0.9
two_anova_p2=0.9
two_anova_p3=0.9
while residuals_shap<=0.05 or residuals_k<=0.05 or two_anova_p1>=0.05 or two_anova_p2>=0.05 or two_anova_p2>=0.05:

    ###Below generates the data and makes it into one array
    male_placebo=np.random.normal(loc=80.0, scale=3.0, size=20)
    male_drug=np.random.normal(loc=20.0, scale=3.0, size=20)
    female_placebo=np.random.normal(loc=80.0, scale=3.0, size=20)
    female_drug=np.random.normal(loc=80.0, scale=3.0, size=20)
    combined_impact=np.append(male_placebo,male_drug)
    combined_impact=np.append(combined_impact,female_placebo)
    combined_impact=np.append(combined_impact,female_drug)
    ###Below tests the residuals for normality
    male_placebo_residual=(male_placebo-np.mean(male_placebo))
    male_drug_residual=(male_drug-np.mean(male_drug))
    female_placebo_residual=(female_placebo-np.mean(female_placebo))
    female_drug_residual=(female_drug-np.mean(female_drug))

    ombined_residuals=np.append(male_placebo_residual,male_drug_residual)    combined_residuals=np.append(combined_residuals,female_placebo_residual)
    combined_residuals=np.append(combined_residuals,female_drug_residual)
    standardized_residuals=combined_residuals/np.std(combined_residuals)
    residuals_shap=shapiro(standardized_residuals)[1]
    residuals_k=stats.kstest(standardized_residuals, 'norm')[1]
    #residuals_k=[stats.kstest(control_residual, 'norm')[1],stats.kstest(one_nM_residual, 'norm')[1],stats.kstest(ten_nM_residual, 'norm')[1],stats.kstest(twenty_nM_residual, 'norm')[1]]
    #print(residuals_shap)
    #print('K',residuals_k)
    ###Below tests the data for homogeneity of variance
    
    col1 = "Sex"
    col2 = 'Treatment'
    col3 = 'Score'
    sex=['Male']*len(male_placebo)+['Male']*len(male_drug)+['Female']*len(female_placebo)+['Female']*len(female_drug)
    treatment=['Placebo']*len(male_placebo)+['Drug']*len(male_drug)+['Placebo']*len(female_placebo)+['Drug']*len(female_drug)


    question_2 = pd.DataFrame({col1:sex,col2:treatment,col3:combined_impact})

    model = ols('Score ~ C(Sex) + C(Treatment) + C(Sex):C(Treatment)', data=question_2).fit()
    result = sm.stats.anova_lm(model, type=2)
    two_anova_p1=result['PR(>F)'][0]
    two_anova_p2=result['PR(>F)'][1]
    two_anova_p3=result['PR(>F)'][2]




### Question 3
## This question will direct the students to do a repeated measures ANOVA


residuals_shap=0.0
residuals_k=0.0
one_way_p_value=0.9
first_tukey_pair=0.0
second_tukey_pair=0.9
third_tukey_pair=0.0
two_anova_p1=0.9
two_anova_p2=0.9
two_anova_p3=0.9
while residuals_shap<=0.05 or residuals_k<=0.05:

    ###Below generates the data and makes it into one array
    control_timepoint=np.random.normal(loc=60.0, scale=3.0, size=20)
    first_timepoint=np.random.normal(loc=70.0, scale=3.0, size=20)
    second_timepoint=np.random.normal(loc=80.0, scale=3.0, size=20)
    third_timepoint=np.random.normal(loc=60.0, scale=3.0, size=20)
    combined=np.append(control_timepoint,first_timepoint)
    combined=np.append(combined,second_timepoint)
    combined=np.append(combined,third_timepoint)
    ###Below tests the residuals for normality
    control_residual=(control_timepoint-np.mean(control_timepoint))
    first_timepoint_residual=(first_timepoint-np.mean(first_timepoint))
    second_timepoint_residual=(second_timepoint-np.mean(second_timepoint))
    third_timepoint_residual=(third_timepoint-np.mean(third_timepoint))
    combined_residuals=np.append(control_residual,first_timepoint_residual)
    combined_residuals=np.append(combined_residuals,second_timepoint_residual)
    combined_residuals=np.append(combined_residuals,third_timepoint_residual)
    standardized_residuals=combined_residuals/np.std(combined_residuals)
    residuals_shap=shapiro(standardized_residuals)[1]
    residuals_k=stats.kstest(standardized_residuals, 'norm')[1]
    #residuals_k=[stats.kstest(control_residual, 'norm')[1],stats.kstest(one_nM_residual, 'norm')[1],stats.kstest(ten_nM_residual, 'norm')[1],stats.kstest(twenty_nM_residual, 'norm')[1]]
    #print(residuals_shap)
    #print('K',residuals_k)
    ###Below tests the data for homogeneity of variance
    
    col1 = "Subject"
    col2 = 'Timepoint'
    col3 = 'Axon Length (nm)'
    subject=list(range(len(control_timepoint)))*4
    timepoint=['Control']*len(control_timepoint)+['First']*len(control_timepoint)+['Second']*len(control_timepoint)+['Third']*len(control_timepoint)


    question_3 = pd.DataFrame({col1:subject,col2:timepoint,col3:combined})

    #model = ols('Score ~ C(Sex) + C(Treatment) + C(Sex):C(Treatment)', data=question_2).fit()
    # Conduct the repeated measures ANOVA
    print(AnovaRM(data=question_3, depvar='Axon Length (nm)', subject='Subject', within=['Timepoint']).fit())



### Question 4
### Below sets up a one way non parametric Anova Kruskal Wallis

residuals_shap=0.9
residuals_k=0.9
one_way_p_value=0.9
first_tukey_pair=0.0
second_tukey_pair=0.9
third_tukey_pair=0.0
pvalue=0.0
while residuals_shap>=0.05 or residuals_k>=0.05 or pvalue<=0.05:

    ###Below generates the data and makes it into one array
    control_axon=stats.uniform.rvs(size=50, loc=0.8, scale=0.1)
    one_nM_axon=stats.uniform.rvs(size=50, loc=0.8, scale=0.1)
    ten_nM_axon=stats.uniform.rvs(size=50, loc=0.8, scale=0.1)
    twenty_nM_axon=stats.uniform.rvs(size=50, loc=0.8, scale=0.1)

    combined_lengths=np.append(control_axon,one_nM_axon)
    combined_lengths=np.append(combined_lengths,ten_nM_axon)
    combined_lengths=np.append(combined_lengths,twenty_nM_axon)
    ###Below tests the residuals for normality
    control_residual=(control_axon-np.mean(control_axon))
    one_nM_residual=(one_nM_axon-np.mean(one_nM_axon))
    ten_nM_residual=(ten_nM_axon-np.mean(ten_nM_axon))
    twenty_nM_residual=(twenty_nM_axon-np.mean(twenty_nM_axon))
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
    pvalue = stats.kruskal(control_axon, one_nM_axon, ten_nM_axon, twenty_nM_axon)[1]

col1 = "Dose:"
col2 = 'Axon Length (nm)'
doses=['Control']*len(control_axon)+['1 nM']*len(one_nM_axon)+['10 nM']*len(ten_nM_axon)+['20 nM']*len(twenty_nM_axon)

question_4 = pd.DataFrame({col1:doses,col2:combined_lengths})

with pd.ExcelWriter('Conference_3/conference_3_dataset.xlsx') as writer:
       
    # use to_excel function and specify the sheet_name and index
    # to store the dataframe in specified sheet
    question_1.to_excel(writer, sheet_name="Question 1", index=False)
    question_2.to_excel(writer, sheet_name="Question 2", index=False)
    question_3.to_excel(writer, sheet_name="Question 3", index=False)
    question_4.to_excel(writer, sheet_name="Question 4", index=False)