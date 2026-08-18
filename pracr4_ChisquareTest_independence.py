import numpy as np 
import scipy.stats as stats

observed = np.array([
    [25,30,15], 
    [30,25,40]
])

print("----Observed----")
print(observed)

row_sum = observed.sum(axis=1)
col_sum = observed.sum(axis=0)

grand_total = observed.sum()

expected = np.outer(row_sum, col_sum) / grand_total
print("----Expected----")
print(expected)

# Exam formula
dof = (observed.shape[0] - 1) * (observed.shape[1] - 1)
chi_2 = (((observed - expected) ** 2) / expected).sum()
p_val = stats.chi2.sf(chi_2, dof)
print("Chi square value:", chi_2)
print("Probability value:", p_val)
# print("Probability value:", dof)

# Only use for correct answer verification and compare your formulated answer with this.
chi_2, p_val, dof, expected = stats.chi2_contingency(observed=observed)
print("Chi square value:", chi_2)
print("Probability value:", p_val)