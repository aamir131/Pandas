import pandas as pd
df = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details31.csv")
print(df)
print()

# default axes = '0'
# this method is used to check NAN values in column if found so drop rows
subset_1 = df.dropna(subset = ['Id'])
print(subset_1)
print()

# default axes = '0'
# this method is used to check NAN values in column if found so drop rows
subset_1 = df.dropna(subset = ['Age'])
print(subset_1)
print()

# default axes = '0'
# this method is used to check NAN values in column if found so drop rows
subset_1 = df.dropna(subset = ['Company '])
print(subset_1)
print()

df1 = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details31.csv")
print(df1)
print()
# this method is used to update dataframe not create new df and drop NAN values row
inplace = df1.dropna(inplace =True)
print(inplace)