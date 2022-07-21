import pandas as pd
df = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details28.csv")
print(df)
print()
# if value not convert in NAN to used keep_default_na
print()
not_change = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details28.csv",keep_default_na=False)
print(not_change)
print()
# if value not convert in NAN to used keep_default_na = False
print()
not_change = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details28.csv",keep_default_na=True)
print(not_change)# if keep_default_na = True this condition is no always NAN
print()