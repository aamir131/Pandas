import pandas as pd

df = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details25.csv")    
print(df)
print()
change_true_value = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details25.csv",true_values=["yes"],false_values=["no"])    
print(change_true_value )


