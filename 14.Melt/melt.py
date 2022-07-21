import pandas as pd 
df = pd.read_csv("E:\\code\\Pandas\\14.Melt\\movie.csv")
print(df)
print()

#This method is used to seprete id variable value and change wide format to long format
df1 = pd.melt(df)
print(df1)
print()
# here used identifier variable
df2 = pd.melt(df,id_vars = ['Gener'])
print(df2)
print()
# here used identifier variable
df2 = pd.melt(df,id_vars = ['Year'])
print(df2)

print()
# here used identifier variable
df2 = pd.melt(df,id_vars = ['Year'],value_vars='Gener')
print(df2)

print()
# here used identifier variable
df2 = pd.melt(df,id_vars = ['Year'],value_vars='Rating %')
print(df2)

print()
# here used identifier variable
df2 = pd.melt(df,id_vars = ['Year'],value_vars='Rating %',var_name='Category')
print(df2)# this method is used to change variable name

print()
# here used identifier variable
df2 = pd.melt(df,id_vars = ['Year'],value_vars='Rating %',var_name='Category',value_name='Data') # this method is used to change value name
print(df2)