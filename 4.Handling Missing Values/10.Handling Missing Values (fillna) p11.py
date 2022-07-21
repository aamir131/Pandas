import pandas as pd
df = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details31.csv")
print(df)
print()

# this method is used to fill the NAN values with given same values(input)
use_scalar = df.fillna(1)
print(use_scalar)
print()
# this method is used to fill the NAN values with given same values(input)
use_scalar2 = df.fillna(5)
print(use_scalar2)
print()
# this method is used to fill the NAN values with given in different column to different values(input)
use_dict = df.fillna({'Id':5,'Age':72,'Company ':'Amazon'})# value para
print(use_dict)
print()

print()
# this method is used to fill the NAN values with forward values(input)
use_ffill = df.fillna(method = 'ffill')# method para
print(use_ffill)
print()
print()
# this method is used to fill the NAN values with forward values(input)
use_ffill = df.fillna(method = 'pad')# same para with ffill
print(use_ffill)
print()

print()
# this method is used to fill the NAN values with backward values(input)
use_bfill = df.fillna(method = 'bfill')# method para
print(use_bfill)
print()

print()
# 0 = rows and 1 = column
# this method is used to fill the NAN values with forward values(input)
use_ffill = df.fillna(method = 'ffill',axis= 0)# method para
print(use_ffill)
print()

# 0 = rows and 1 = column
# this method is used to fill the NAN values with forward values(input)
use_ffill = df.fillna(method = 'ffill',axis= 1)# method para
print(use_ffill)
print()