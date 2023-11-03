
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
### Below sets up a normally distributed corrleation between two variables

MHPG_shap=0.0
MHPG_k=0.0

score_shap=0.0
score_k=0.0

while MHPG_shap <= 0.05 or MHPG_k <= 0.05 or score_shap <= 0.05 or score_k <= 0.05:

    rng = np.random.default_rng()
    s = 0.5
    MHPG= stats.norm.rvs(size=500, random_state=rng)
    e = stats.norm.rvs(scale=s, size=500, random_state=rng)
    score = MHPG + e

    MHPG_shap = shapiro(MHPG)[1]
    MHPG_k = stats.kstest(MHPG, 'norm')[1]
    score_shap = shapiro(score)[1]
    score_k = stats.kstest(score, 'norm')[1]



col1 = "MHPG Levels"
col2 = 'Scores'
#doses=['Control']*len(control_water_maze)+['1 nM']*len(one_nM_water_maze)+['10 nM']*len(ten_nM_water_maze)+['20 nM']*len(twenty_nM_water_maze)

question_1 = pd.DataFrame({col1:MHPG,col2:score})


### Question 2

# Simulating data for the study
brain_size = np.random.normal(50, 10, 100)
drug_effect = np.random.normal(5, 2, 100)
neuro_score = 0.5 * brain_size + 2 * drug_effect + np.random.normal(0, 5, 100)
neuro_score[neuro_score < 0] = 0  # ensuring no negative scores

# Creating a DataFrame
df = pd.DataFrame({'Brain_Size': brain_size, 'Drug_Effect': drug_effect, 'Neuro_Score': neuro_score})

# ANCOVA analysis
model = ols('Neuro_Score ~ Brain_Size + Drug_Effect', data=df).fit()
print(model.summary())

with pd.ExcelWriter('Conference_5/conference_5_dataset.xlsx') as writer:
       
    # use to_excel function and specify the sheet_name and index
    # to store the dataframe in specified sheet
    question_1.to_excel(writer, sheet_name="Question 1", index=False)
