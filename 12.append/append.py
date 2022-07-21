import pandas as pd 
df1 = pd.DataFrame({'A':[1,2,3,4],'B':[11,22,33,44]})
print(df1)
print()
df2 = pd.DataFrame({'A':[5,6,7,8],'B':[55,66,77,88]})
print(df2)
print()
# this method is used to append df
appen = df1.append(df2)
print(appen)
print()

# this method is used to ignor index
ignore_index = df1.append(df2,ignore_index = True)
print(ignore_index)
print()

# this method is used to change position
chang_posi = df2.append(df1,ignore_index = True)
print(chang_posi)
print()

# this method is used to deffirent column name
df3 = pd.DataFrame({'C':[9,10,11,12],'B':[99,11,12,13]})
chang_posi = df1.append(df3,ignore_index = True)
print(chang_posi)