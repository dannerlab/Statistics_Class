import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.formula.api as smf

N_sub = 10
N_sample = 10
N_groups = 3
means = [15.,15.,16.]
var_sub = 5.
var_gen = 1.
p_drop = 0.5

data = []
for i in range(N_sub):
  sub_offset = np.random.normal(0,var_sub)
  for j in range(N_groups):
    if j>0 and np.random.uniform() < p_drop:
      print('dropped',i,j)
      continue
    for k in range(N_sample):
      data.append({"subject":i,"group":j,"sample":k,"value":np.random.normal(means[j],var_gen)+sub_offset})

df = pd.DataFrame(data)


print(stats.f_oneway(*[df[df["group"]==i]["value"] for i in range(N_groups)]))
print(df.groupby("group")["value"].mean(),df.groupby("group")["value"].std())

md = smf.mixedlm("value ~ group", df, groups=df['subject'])
mdf = md.fit()
print(mdf.summary())
print(var_sub**2/(var_sub**2+var_gen**2))

sns.boxenplot(x="group",y="value",hue="subject",data=df)
plt.show()
df.to_excel("mixed_model.xlsx")

df_rm = df.groupby(['subject','group']).value.mean().unstack()
df_rm.to_excel("mixed_model_rm.xlsx")