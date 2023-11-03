import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Generating synthetic data
np.random.seed(0)

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