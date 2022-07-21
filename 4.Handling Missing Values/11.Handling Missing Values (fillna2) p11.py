import pandas as pd
df = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details31.csv")
print(df)
print()

# 0 = value and 1 = how many place
# this method is used to fill specific NAN values 
use_limit = df.fillna(0,limit = 1)# method para
print(use_limit)
print()
# 5 = value and 2 = how many place
# this method is used to fill specific NAN values 
use_limit = df.fillna(5,limit = 2)# method para
print(use_limit)
print()
# ffill = forward value and 2 = how many place
# this method is used to fill specific NAN values 
use_ffill_limit = df.fillna(method = 'ffill',limit = 2)# method para
print(use_ffill_limit)
print()

# 10 =  value 
# this method is used to update or modify NAN values 
use_ffill_inplace = df.fillna(10,inplace = False)# method para
print(use_ffill_inplace)
print()