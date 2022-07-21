import pandas as pd

df = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details22.csv")    
#print(df)
print()
head_method = df.head() #this method is used to read first five rows
print(head_method)
print()
head_method1 = df.head(2) #this method is used to read specific rows
print(head_method1)
print()


