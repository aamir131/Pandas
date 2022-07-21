import pandas as pd
df = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details26.csv")
print(df)
print()
na_values = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details26.csv")
print(na_values)
print()
na_values1 = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details27.csv")
print(na_values1)# This method is not handel not available
print()
# this method is used how to handel using na_values
na_values2 = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details27.csv",na_values="not available")
print(na_values2)
print()
# this method is used to handle missing values like not available,no value, unavailable
na_values2 = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details27.csv",na_values=["not available","Unavailable"]) # handle using list
print(na_values2)

print()
# this method is used to handle missing values like not available,no value, unavailable
na_values2 = pd.read_csv("E:\\code\\Pandas\Handling Missing Values\\Bill_details27.csv",na_values={'Networth':'Unavailable','Address':'not available'})# handle using dictionary
print(na_values2)