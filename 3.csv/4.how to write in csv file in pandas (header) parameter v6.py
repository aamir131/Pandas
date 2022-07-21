import pandas as pd

df = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details23.csv")
print(df)
print()
# this method is used to change header using header parameter
change_header = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details23.csv",header=1)
print(change_header)
print()

df2 = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details24.csv")
print(df2)
print()

# this method is used to change header using header parameter
change_header2 = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details24.csv",header=2)
print(change_header2)
print()
# this method is used to change header using header parameter
change_header3 = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details24.csv",header=None)
print(change_header3)
print()