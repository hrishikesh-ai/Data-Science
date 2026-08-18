import pandas as pd;
import numpy as np;
from scipy import stats

df = pd.read_csv('College.csv')
n = 5
k = len(df.columns)
ves = np.array(df["VESASC"])
nga = np.array(df["NGA"])
bt = np.array(df["BT"])

vmean = np.mean(ves)
nmean = np.mean(nga)
bmean = np.mean(bt)

omean = (vmean + nmean + bmean)/k

ssb = n*((vmean-omean)**2+(nmean - omean)**2 + (bmean - omean)**2)
dfk = k - 1
var_btw_grps = ssb / dfk
print(var_btw_grps)

# Finding errors in groups
err_ves = ves - vmean
err_nga = nga - nmean
err_bt = bt - bmean

all_grp_errs = np.concatenate((err_ves, err_nga, err_bt), axis=0)
print(all_grp_errs)

# Finding sum of squares of errors within groups
ssw = 0

for i in all_grp_errs:
    ssw += i**2

dfn = k* (n - 1)
var_in_grps = ssw / dfn
print(var_in_grps)

F = var_btw_grps / var_in_grps
p_val = stats.f.sf(F, dfk, dfn)
print(f"F: {F}, P-val: {p_val}")
F, p_val = stats.f_oneway(ves, nga, bt)
print(f"F: {F}, P-val: {p_val}")