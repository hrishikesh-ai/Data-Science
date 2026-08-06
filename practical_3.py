# import pandas as pd 
# from sklearn.preprocessing import MinMaxScaler, StandardScaler

# df = pd.read_csv("wine.csv",header=None, usecols=(0,1,2), skiprows=1)
# df.columns = ['Class', 'Alcohol_level', 'Malic_Acid']
# print(df)

# print("Scaling using Min-Max Scalar")
# mn_scaler = MinMaxScaler()

# df[col_name]= mn_scaler.fit_transform(df[['Class', 'Alcohol_level', 'Malic_Acid']])
# print(df)


# print('Scaling Using Standard Scalar')
# ss = StandardScaler()
# df[['Class', 'Alcohol_level', 'Malic_Acid']]=ss.fit_transform(df[['Class', 'Alcohol_level', 'Malic_Acid']])
# print(df)


import pandas as pd 
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv("wine.csv",header=None, usecols=(0,1,2,3,4), skiprows=1)
col_name = ["SLenght", "SWidth", "PLenght", "PWidth", "Species"]
df.columns = col_name
print(df)

print("Scaling using Min-Max Scalar")
mn_scaler = MinMaxScaler()

df[col_name]= mn_scaler.fit_transform(df[col_name])
print(df)


print('Scaling Using Standard Scalar')
ss = StandardScaler()
df[col_name]=ss.fit_transform(df[col_name])
print(df)