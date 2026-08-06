import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('iris-id.csv')

print("Id Column with Label Encoder")
le = LabelEncoder()

df['ID']= le.fit_transform(df["species"])
print(df)


# dummy = pd.get_dummies(df, columns=["species"], drop_first= False, dummy_na = False,dtype=int)
# print(dummy[["sepal_length","sepal_width","petal_length","petal_width","species"]])

dummy = pd.get_dummies(df, columns=["species"], drop_first=False, dummy_na = False,dtype=int)