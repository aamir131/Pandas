import pandas as pd
import numpy as np 
se = pd.Series([1,2,np.nan,4,np.NAN,6])
print(se)
print()
# if output is false so no NAN value in Data set
is_null = se.isnull()
print(is_null)

print()
# this method is used to check how many null values
is_null_sum = se.isnull().sum()
print(is_null_sum)
print()
# this method is used to check total null values 
is_null_sum_sum = se.isnull().sum().sum()
print(is_null_sum_sum)
