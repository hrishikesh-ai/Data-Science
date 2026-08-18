import numpy as np
import scipy.stats as stats

observed = np.array([12,10,8,10,11,9])
print("Onserved frequency:", observed)

faces = len(observed)
dof = faces - 1
expected = np.array([observed.sum()/faces] * faces)
print("Expected Frequency:", expected)

chi_2 = sum(((observed - expected) ** 2) / expected)
p_val = stats.chi2.sf(chi_2, df=dof)
print("Chi Square value:", chi_2)
print("Probability:", p_val)

chi_2, p_val = stats.chisquare(f_obs=observed, f_exp=expected)
print(f"Ready made formula: {p_val}")