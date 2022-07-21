import pandas as pd 
df = pd.read_csv("E:\\code\\Pandas\\loc iloc\\Student_data1.csv")
print(df)
print()
# this method is used to read 0 index data
iloc0 = df.iloc[0]
print(iloc0)
print()
# this method is used to slice
iloc_slice1 = df.iloc[:2] # 0:1 0 = rows,1 = column
print(iloc_slice1)
print()
iloc_boo = df.iloc[[True,False,True,True,False,True,True,False,True]]
print(iloc_boo)