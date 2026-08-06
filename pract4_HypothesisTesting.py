import numpy as np
from scipy import stats

print("HO: Mean Age >= 19")
print("H1: Mean Age < 19")
# x = 18
# u = 19 
# pSD = 2.1
# n = 40 
# sl = 0.05
x = int(input("Enter the Value For x: "))
u = int(input("Enter the Value For u: "))
pSD = float(input("Enter the Value For pSD: "))
n = int(input("Enter the Value For n: "))
sl = float(input("Enter the Value For sl: "))

z = (x-u)/(pSD/np.sqrt(n))
print(z)
p = stats.norm.cdf(z)
print(p)

if p > sl:
    print("We accept Null Hypothesis")
else:
    print("We accept Null Hypothesis")