import pandas as pd
df = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details29.csv")
print(df)
print()
# this parameter is used to boost performane if no any none value
print()
not_change = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details29.csv",na_filter=False)
print(not_change)
print()
print()
not_change = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details29.csv",na_filter=True)
print(not_change)
print()