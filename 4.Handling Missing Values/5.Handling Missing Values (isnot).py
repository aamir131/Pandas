import pandas as pd
df = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details29.csv")
print(df)
print()
# this method is used to check NAN value 
# if output is false so NAN or no value in Data set
not_null = df.notnull()
print(not_null)
print()
# if output is true so correct value in Data set
df1 = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details30.csv")
print(df1)
print()
not_null1 = df1.notnull()
print(not_null1)
print()
# this method is used to check how many correct values and which column
print()
not_null2 = df1.notnull().sum()
print(not_null2)
print()

# this method is used to check total correct values 
print()
not_null3 = df1.notnull().sum().sum()
print(not_null3)
print()