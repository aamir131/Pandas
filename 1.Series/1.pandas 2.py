import pandas as pd
print(pd.__version__) # this method is used to check pandas version
print()
list_p = [1,2,4.6,"list value"]#this list method
print(list_p)

print()
series1 = pd.Series(list_p) #this is series method
print(series1)
series2 = pd.Series([1,3,5,6.7])# this method is used 