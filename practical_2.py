import pandas as pd

df = pd.read_csv("employee_records.csv")

# 1. Handle missing Values using fillna and dropna.
df.dropna(inplace = True)
df.fillna(value=0, inplace=True)

# 2. Filter Salary column to show employees with salary higher than 40K.
print()
print(df[df['Salary'] > 40000])

# 3. Filter Designation to show only Marketing Employees.
print()
print(df[df['Department']== "Marketing"].get("Designation"))

# 4. Sort the employee names in forward and reverse order.
print()
print(df[df["Emp_Name"] == sorted(df['Emp_Name'])])
print(df[df["Emp_Name"] == sorted(df['Emp_Name'], reverse=True)])

# 5. Display only Tech emplopyees.
print()
print(df[df["Department"]=="Tech"])

# 6. Find the Average salary of all departments.


# 7. Find the count of HR empoyees


# 8. Find the designation wise highest and lowest salary.
