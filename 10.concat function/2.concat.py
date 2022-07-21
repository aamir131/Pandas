import pandas as pd 
# this method is used to create df using dict
df1 = pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[7,8,9,10]})
print(df1)
print()
df2 = pd.DataFrame({'ID':[11,22,33],'Name':['K','L','M',],'Class':[5,6,7]})
print(df2)
print()
con_df = pd.concat([df1,df2])# row wise using objs para
print(con_df)
print()
col_con_df = pd.concat([df1,df2],axis=1) # column wisw using axis para
print(col_con_df)
print()
join_con_df = pd.concat([df1,df2],axis=1,join='inner') # print only not NAN value using join para
print(join_con_df)
print("join_axes1")
join_con_df = pd.concat([df1,df2], axis=1, join_axes=[df1.index]) # this method is used to print specific index
print(join_con_df)

print("join_axes")
join_con_df = pd.concat([df1,df2], axis=1, join_axes=[df2.index]) # this method is used to print specific index
print(join_con_df)