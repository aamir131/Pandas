import pandas as pd 
df1 = pd.DataFrame({'A':[1,2,3],'B':[11,22,33]})
print(df1)
print()
df2 = pd.DataFrame({'C':[4,5,6],'D':[44,55,66]})
print(df2)
print()
# this method is used to join 2 df
join_df = df1.join(df2)
print(join_df)
print()
df3 = pd.DataFrame({'C':[4,6],'D':[44,66]})
print(df3)
print()
# this method is used to join 2 df
join_df = df1.join(df3)
print(join_df)
print()

# this method is used to join 2 df
join_left_df = df1.join(df3,how='left')
print(join_left_df)
print()
# this method is used to join 2 df
join_df = df1.join(df3,how='right')
print(join_df)
print()
# this method is used to join 2 df
join_df = df1.join(df3,how='inner')
print(join_df)
print()
# this method is used to join 2 df
join_df = df1.join(df3,how='outer')
print(join_df)
print()


# if same column name
df3 = pd.DataFrame({'C':[4,6],'D':[44,66]})
print(df3)
print()
df4 = pd.DataFrame({'C':[7,99],'E':[77,99]})
print(df4)
print()
join_same_col = df3.join(df4,lsuffix='_l',rsuffix='_r')# if same column name so used lsuffix and rsuffix
print(join_same_col)