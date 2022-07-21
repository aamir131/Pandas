#pandas series using Numpy
import pandas as pd
s = pd.Series([1,2,3,4,5])
print(s)
print()
s1 = pd.Series([6,7,8,9,10])
print(s1)
print()
s3 = s+s1 # this mathod is used to  add 2 equal data value series
print(s3)
print()
s4 = pd.Series(1,2,3,4)
print(s4)
print()
add_unequal = s+s1 # this mathod is used to  add 2 unequal data value series
print(add_unequal)
