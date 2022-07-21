import pandas as pd

df = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details23.csv")
print(df)
print()
# this method is used to change header using header parameter
# if none header change to string header
# so this method is used both parameter header and prefix but Header =None
prefix_data = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details23.csv",header=None,prefix="Data")
print(prefix_data)
print()
# this method is used to change header using header parameter
# if none header change to string header
# so this method is used both parameter header and prefix but Header =None
prefix_col = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details23.csv",header=None,prefix="Columns")    # this method all col name same
print(prefix_col)
print()
# this method is used to change header using header parameter
# if none header change to string header
# so this method is used both parameter header and prefix but Header =None
prefix_col = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details23.csv",header=None,prefix="Columns")    # this method all col name same
print(prefix_col)
print()


