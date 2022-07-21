import pandas as pd
df = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details31.csv")
print(df)

print()
# default axes = '0'
# this method is used to check atleast 1 not null value  
thresh_1 = df.dropna(thresh = 1)
print(thresh_1)
print()
# default axes = '0'
# this method is used to check atleast 2 not null value  
thresh_1 = df.dropna(thresh = 2)
print(thresh_1)
print()
# default axes = '0'
# this method is used to check atleast 1 not null value otherwise drop rows
thresh_1 = df.dropna(thresh = 4)
print(thresh_1)
