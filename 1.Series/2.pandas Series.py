import pandas as pd
print(pd.__version__) # this method is used to check pandas version
print()

list_p = [1,2,4.6,"list value"]#this is list method
print(list_p)

print()
series1 = pd.Series(list_p) #this is series method and in this method index is default
print(series1)
print()

series2 = pd.Series([1,3,5,6.7])# this method is used create series using short method
print(series2)

print()

empty_s = pd.Series([]) # this method is used create empty series
print(empty_s)

print()

change_index = pd.Series([1,3,5,8],index = ['a','b','c','d'])# this method is used to change index no.
print(change_index)

print()

change_dtype = pd.Series([1,3,5,8],index = ['a','b','c','d'],dtype = float)# this method is used to change data type
print(change_dtype)
print()
# this method is used to give the name of data value
givename_datavalue = pd.Series([1,3,5,8],index = ['a','b','c','d'],dtype = float,name = "data value")
print(givename_datavalue)
print()