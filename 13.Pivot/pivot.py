import pandas as pd 
df1 = pd.read_csv("E:\\code\\Pandas\\13.Pivot\\movie.csv")
print(df1)
print()
# here applied pivot table
df = df1.pivot_table(index='Year')# row wise mean value
print(df)
print()
df2 = df1.pivot_table(index='Gener',columns= 'Year')# column wise mean value
print(df2)
print()
df3 = df1.pivot_table(index='Gener',columns= 'Year',aggfunc = 'count')# column wise mean value
print(df3)
print()
df3 = df1.pivot_table(index='Gener',columns= 'Year',aggfunc = 'sum')# column wise mean value
print(df3)
# fill para is used to fill NAN value
print()
fill_NAN = df1.pivot_table(index='Gener',columns= 'Year',fill_value = 0)
print(fill_NAN)
# this method is used to add all row and column like grand total
print()
marg = df1.pivot_table(index='Gener',columns= 'Year',fill_value = 0,margins = True)
print(marg)

print()
marg = df1.pivot_table(index='Gener',columns= 'Year',aggfunc = 'sum',fill_value = 0,margins = True)
print(marg)