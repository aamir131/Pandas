import pandas as pd
df = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details29.csv")
print(df)
print()
# this method is used to check NAN value 
# if output is false so no NAN value in Data set
is_null = df.isnull()
print(is_null)
print()
# if output is true so NAN or no value in Data set
df1 = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details30.csv")
print(df1)
print()
is_null1 = df1.isnull()
print(is_null1)
print()
# this method is used to check how many null values and which column
print()
is_null2 = df1.isnull().sum()
print(is_null2)
print()

# this method is used to check total null values 
print()
is_null3 = df1.isnull().sum().sum()
print(is_null3)
print()