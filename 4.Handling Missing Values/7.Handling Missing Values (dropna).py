import pandas as pd
df = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details31.csv")
print(df)
print()
# this method is used to drop rows in which NAN valuse 
drop = df.dropna()
print(drop)
print()
# default axis =0
# this method is used to drop columns in which NAN valuse 
axis = df.dropna(axis = 1)# 0 means rows and 1 means column
print(axis)
print()
# default how = 'any'
# this method is used to drop columns or rows in which NAN valuse 
how = df.dropna(how = 'any')# thid method is same drop
print(how)

print()
# default how = 'any'
# this method is used to drop columns or rows in which NAN valuse 
same_with_axis = df.dropna(axis = 1,how = 'any')# thid method is same axis
print(same_with_axis)

print()
# default how = 'any'
# this method is used to drop columns or rows in which NAN valuse 
how = df.dropna(how = 'all')# thid method is same df
print(how)