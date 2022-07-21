import pandas as pd 
df = pd.read_csv("E:\\code\\Pandas\\DatetimeIndex\\ido.csv")
print(df)
print()
# this method is used to check type of df
type_ = df.dtypes
print(type_)
print()
# this method is used to check type of date column
type_ = type(df.Date[0])
print(type_)
# this method is used to change dtype of dae column
chang = pd.read_csv("E:\\code\\Pandas\\DatetimeIndex\\ido.csv",parse_dates=['Date'])
print(chang)
print()
# this method is used to check type of df
type_d = chang.dtypes
print(type_d)
print()

# this method is used to check type of date column
type_ = type(chang.Date[0])
print(type_)