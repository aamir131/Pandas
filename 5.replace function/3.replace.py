import pandas as pd 
df = pd.read_csv("E:\\code\\Pandas\\5.replace function\\Student_data.csv")
print(df)
print()
# this method is used to replace forward value  
# and this method is also used as with parameter
method = df.replace('Larry',method = 'ffill')
print(method)
print()
# this method is used to replace forward value  
# and this method is also used as with parameter
method = df.replace('Larry',method = 'bfill')
print(method)
print()
# this method is used to replace backward value 
# limit method is used to how many value are replace 
# and this method is also used as with parameter
method = df.replace(15500,method = 'bfill',limit = 1)
print(method)
# this method is used to replace backward value 
# limit method is used to how many value are replace 
# and this method is also used as with parameter
method = df.replace(15000,method = 'bfill',limit = 2)
print(method)
print()
print(df)
# this method is used to modify value 
# 15000 = old value
# 100 = new value 
# and this method is also used as with parameter
method = df.replace(15000,100,inplace = False)
print(method)
print()
print(df)