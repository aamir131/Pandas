import pandas as pd

df = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details22.csv")    
print(df)
print()
change_dtype = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details22.csv",dtype={"Id":float})    
print(change_dtype)


