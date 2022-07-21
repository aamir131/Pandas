import pandas as pd 
# this method is used to create series
se1 = pd.Series([1,2,3])
print(se1)
print()
se2 = pd.Series([4,5,6,7])
print(se2)
print()
#this method is used to concat two series
se3 = pd.concat([se1,se2])
print(se3)
print()

# this method is used to create df using dict
df1 = pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[7,8,9,10]})
print(df1)
print()
df2 = pd.DataFrame({'ID':[11,22,33,44],'Name':['K','L','M','N'],'Class':[5,6,7,11]})
print(df2)
print()
#concat default axis = 0 means row, 1 means column
con_df = pd.concat([df1,df2])# this method is used to concat one or more dataframe
print(con_df)# here concat row wise
print()
#concat default axis = 0 means row, 1 means column
con_df2 = pd.concat([df2,df1],axis=1)# this method is used to concat one or more dataframe
print(con_df2)# here concat column wise
print()
#concat default axis = 0 means row, 1 means column
inde_con_df = pd.concat([df1,df2],ignore_index = True)# this para is used to ignore index no.
print(inde_con_df)# here concat row wise
print()