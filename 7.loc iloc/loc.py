import pandas as pd 
df = pd.read_csv("E:\\code\\Pandas\\loc iloc\\Student_data1.csv")
print(df)
print()
# this method is used to read 0 index data
loc0 = df.loc[0]
print(loc0)
print()
# this method is used to read 3 index data
loc3 = df.loc[3]
print(loc3)
print()
# this method is used to read specific value using row index and column name
loc_speci = df.loc[4,'Class']
print(loc_speci)
print()
# this method is used to slice
loc_slice1 = df.loc[4:9,'Fees']
print(loc_slice1)
print()
# this method is used to slice
loc_slice = df.loc[4:9,'ID']
print(loc_slice)
print("boolean")
# this method is used to boolean list with same length as the row axis
loc_boo = df.loc[[False,False,True,False,False,False,True,False,True,]]
print(loc_boo)
print("condi")
# this method is used to conditional operator
loc_cond = df.loc[df['Roll No.']<12]
print(loc_cond)
print()
# this method is used to conditional operator and read 1 specific column
loc_cond = df.loc[df['Roll No.']<12,['Percentage']]
print(loc_cond)