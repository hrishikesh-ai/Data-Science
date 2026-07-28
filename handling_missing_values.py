# Practical 2

# with open("data.csv") as file:
#     for line in file.readlines():
#         [name, uClass, marks] = line.split(",")
#         print(name or "None", uClass or "None", marks or 0)

import pandas as pd

data = pd.read_csv("data.csv")
print("-"*20 + "Head" + "-"*20)
print(data.head(10))
print("\n" + "-"*20 + "Tail" + "-"*20)
print(data.tail(10))

print("\n" + "-"*20 + "Drop NA" + "-"*20)
data.dropna(inplace=False)
print(data.head(10))

print("\n" + "-"*20 + "Fill NA" + "-"*20)
data.fillna(value=0, inplace=True)
print(data.head(10))

print("\n" + "-"*20 + "Filtering: TYCS" + "-"*20)
copy_tycs = data['Class'] == "TYCS"
print(copy_tycs)

print("\n" + "-"*20 + "Filtering: Marks > 500" + "-"*20)
uMarks = data['Marks']  > 450
print(uMarks)

print("\n" + "-"*20 + "Sorting" + "-"*20)
sorted_names = sorted(data['Name'])
print(sorted_names)

print("\n" + "-"*20 + "Reverse Sorting" + "-"*20)
sorted_names = sorted(data['Name'], reverse=True)
print(sorted_names)