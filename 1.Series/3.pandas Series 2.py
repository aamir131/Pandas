import pandas as pd
# this method is used to create series using scalar 
scalar_se = pd.Series(13)
print(scalar_se)
print()
# this method is used to create single scalar value series multiple time
scalar_se = pd.Series(13,index = [0,1,2,3])
print(scalar_se)
print()
# this method is used to create series using dictionary
dict_se = pd.Series({"a":1, "b":5}) # here alphabate are key and number are value 
print(dict_se)
print()