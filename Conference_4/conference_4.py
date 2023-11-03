from scipy.stats import chi2_contingency

# create a contingency table
observed = [[10, 20, 30, 15], [6, 9, 17, 15], [6, 9, 17, 15]]

# run the chi-squared test
chi2, p, dof, expected = chi2_contingency(observed)

# print the results
print("Chi-squared statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies:", expected)
