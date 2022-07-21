#pandas series using Numpy
import pandas as pd
series = pd.Series([1,2,3,4,5,6])
print(series)
print()
s = series[1]   # this method is used to get one value in series
print(s)
print()
s1 = series[0:3]    # this is a slice method is used to slizing value and not include endpoint
print(s1)
print()
max_v = max(series) # this function is used to get max value in series
print(max_v)
print()
min_v = min(series) # this function is used to get min value in series
print(min_v)
print()
range_v = (series>3) # this methois conditional operator is used to get  value if greater than 3 in series
print(range_v)