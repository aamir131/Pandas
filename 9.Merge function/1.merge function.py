import pandas as pd 
df1 = pd.DataFrame({'ID':[1,2,3,4],'Class':[9,10,11,12]})
print(df1)
print()
df2 = pd.DataFrame({'ID':[1,2,3,5],'Section':['A','B','C','D']})
print(df2)
print()
# this method is used to merge df=dataframe 
mer = pd.merge(df1,df2,on = 'ID')
print(mer)
print()
mer = pd.merge(df2,df1,on = 'ID')
print(mer)

print()
mer = pd.merge(df2,df1,on = 'ID',how = 'left')
print(mer)
print()
mer = pd.merge(df1,df2,on = 'ID',how = 'right')
print(mer)
print()
mer = pd.merge(df1,df2,on = 'ID',how = 'outer')
print(mer)
print()
# indicator para used for know each row information
mer = pd.merge(df1,df2,on = 'ID',how = 'outer',indicator=True)
print(mer)

df3 = pd.DataFrame({'ID':[6,7,8,9],'Section':['A','B','C','D']})
print(df3)
print()
# this para is used to read different different column 
mer2 = pd.merge(df1,df3,left_index = True,right_index = True)
print(mer2)
print()
# this para is used to read different different column 
mer2 = pd.merge(df1,df3)
print(mer2)
print()
df4 = pd.DataFrame({'ID':[1,2,3,4],'Class':[9,10,11,12]})
print(df4)
print()
# this method is used to merge same df
mer4 = pd.merge(df1,df4,on = 'ID')
print(mer4)
# this method is used to change name of same df
mer4 = pd.merge(df1,df4,on = 'ID',suffixes = ('_Higher','_Lower'))
print(mer4)