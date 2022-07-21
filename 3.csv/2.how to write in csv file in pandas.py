import pandas as pd
re_de = pd.read_csv("E:\\code\\Pandas\\3.csv\\Reachest details.csv")
print(re_de)
print(type(re_de))# this method is used to check dtype
print()
print(re_de.columns)    # this method is used to check columns name in table
print()
# this method is used to read no.of rows 
read_specific_rows = pd.read_csv("E:\\code\\Pandas\\3.csv\\Reachest details.csv",nrows=3)
print(read_specific_rows)
print()
# this method is used to read any specific columns to using index no
read_specific_col = pd.read_csv("E:\\code\\Pandas\\3.csv\\Reachest details.csv",usecols=[2])
print(read_specific_col)
print()
# this method is used to print read no.of columns 
read_specific_col = pd.read_csv("E:\\code\\Pandas\\3.csv\\Reachest details.csv",usecols=[0,1,2])
print(read_specific_col)
print()
# this method is used to read any specific imp columns to using index no
read_specific_col = pd.read_csv("E:\\code\\Pandas\\3.csv\\Reachest details.csv",usecols=[0,1])
print(read_specific_col)
print()

re_de = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details.csv")
print(re_de)
print() 
# this method is used to skip 1 rows in table
skip_rows1 = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details.csv",skiprows=1)
print(skip_rows1)
print()
# this method is used to skip no.of rows in table
# 2 rows are skip
skip_rows2 = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details.csv",skiprows=2)
print(skip_rows2)
print()
# this method is used to skip any specific rows from table using index no.
skip_rows_using_index = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details.csv",skiprows=[0])
print(skip_rows_using_index)
print()
# this method is used to skip multiple rows from table using index no.
skip_rows_using_index = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details.csv",skiprows=[0,2,4])
print(skip_rows_using_index)
print()