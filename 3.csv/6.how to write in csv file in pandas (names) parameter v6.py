import pandas as pd

# this method is used to change name using header parameter
name_col = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details23.csv",names=["ID","Name","Networth","AGE","Company"])    # this method all col name different
print(name_col)
print()


