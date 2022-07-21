import pandas as pd 
# this method is used to create df using dict
df1 = pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[7,8,9,10]})
print(df1)
print()
df2 = pd.DataFrame({'ID':[11,22,33,44],'Name':['K','L','M','N'],'Class':[5,6,7,11]})
print(df2)
print()
# this para is used to seprate df or lavel 
key_df = pd.concat([df1,df2],keys=['1st','2nd'])#row wise
print(key_df)
print()
# this para is used to seprate df or lavel 
key_df = pd.concat([df1,df2],axis = 1,keys=['1st','2nd'])# col
print(key_df)
df3 = pd.DataFrame({'Marks':[56,78,90,89]})
print(df3)
print()
con_differ_df = pd.concat([df1,df3])
print(con_differ_df)