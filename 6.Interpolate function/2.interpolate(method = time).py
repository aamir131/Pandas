import pandas as pd 
df = pd.read_csv("E:\\code\\Pandas\\6.Interpolate function\\Student_data1.csv")
print(df)

print()
# method default = linear
# this method is used but df dtype = datetime formate
time1 = df.interpolate(method = 'time')
print(time1)
print()
# this method is used to check dtype
dtype_che = type(df.Date[0])
print(dtype_che)
print()
# this method is used to change dtype convert str to datetime formate
df1 = pd.read_csv("E:\\code\\Pandas\\6.Interpolate function\\Student_data1.csv",parse_dates=['Date'])
print(df1)
print()
# this method is used to check dtype
dtype_che = type(df.Date[0])
print(dtype_che)
print()
print()
# this method is used to change dtype convert str to datetime formate
df1 = pd.read_csv("E:\\code\\Pandas\\6.Interpolate function\\Student_data1.csv",parse_dates=['Date'])
print(df1)
print()
time_d = df1.interpolate(method = 'time')
#print(time_d)