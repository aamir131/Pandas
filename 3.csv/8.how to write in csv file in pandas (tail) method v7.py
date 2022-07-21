import pandas as pd

df = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details22.csv")    
#print(df)
print()
tail_method = df.tail() #this method is used to read last five rows
print(tail_method)
print()
tail_method1 = df.tail(2) #this method is used to read no of rows
print(tail_method1)
print()


