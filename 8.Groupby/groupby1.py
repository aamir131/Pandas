import pandas as pd 
df = pd.read_csv("E:\\code\\Pandas\\8.Groupby\\Student_data1.csv")
print(df)
print()
# this method is used to group same element in a column
gr1 = df.groupby(by = 'Fees')
print(gr1)
gr2 = gr1.groups
print(gr2)
print()
# this method is used to group two column
gr3 = df.groupby(['Roll No.','Class']).groups
print(gr3)
print()
for Fees, df_2 in gr1:
    print(Fees)
    print(df_2)
print()
# this method is used to convert in list
list_ = list(gr1)
print(list_)
print()
# this method is used to convert in list to dict
dict_ = dict(list(gr1))
print(dict_)
print()
# this method is used to group according to class
gr6 = df.groupby('Class').get_group(10)
print(gr6)
print()
# this method is used to group according to Roll No.
gr7 = df.groupby('Roll No.').get_group(10)
print(gr7)
print()
# this method is used to add element
gr8 = gr6.sum()
print(gr8)
print()
# this method is used to find mean an element
gr9 = gr6.mean()
print(gr9)
print()
# this method is used to find describe an element
gr9 = gr6.describe()
print(gr9)
print()
# this is a multiple function
gr10 = gr6.agg(['sum','max','mean'])
print(gr10)