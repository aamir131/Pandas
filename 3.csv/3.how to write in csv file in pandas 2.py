import pandas as pd

df = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details22.csv")
print(df)
print() 
#this method is used to change or replace Id column as index no.
id_col_to_index = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details22.csv",index_col="Id")
print(id_col_to_index)
print()  

print() 
#this method is used to change or replace Name column as index no.
name_col_to_index = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details22.csv",index_col="Name")
print(name_col_to_index)
print() 
print() 
#this method is used to change or replace Age column as index no.
age_col_to_index = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details22.csv",index_col="Age")
print(age_col_to_index)
print()

#this method is used to change or replace Age column as index no.
age_col_to_index = pd.read_csv("E:\\code\\Pandas\\3.csv\\Bill_details22.csv",index_col=3)
print(age_col_to_index)
print()