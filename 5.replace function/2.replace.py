import pandas as pd 
df = pd.read_csv("E:\\code\\Pandas\\5.replace function\\Student_data.csv")
print(df)
print()

# this method is used to replace lot of values to different different value using list
# and this method is also used as without parameter

replace_lot_def = df.replace([101,102,103,104,105,106,107,108,109],[1,2,3,4,5,6,7,8,9]) #used as integer
print(replace_lot_def)
print()

# this method is used to replace a specific value in specific column usig dict
# and this method is also used as with parameter

replace_dict = df.replace({'Name':'Larry'},0) #used as integer
print(replace_dict)
print( )
# this method is used to replace multiple column value to any specific value usig dict
# and this method is also used as with parameter

replace_dict2 = df.replace({'Name':'Larry','Fees':20000},000) #used as integer
print(replace_dict2)
print()
# this method is used to replace all string value to any specific value 
# and this method is also used as with parameter

replace_regex = df.replace('[A-Za-z]',0,regex = True) #used as integer
print(replace_regex)
# this method is used to replace any specific column string value to any specific value using dict 
# and this method is also used as with parameter

replace_regex = df.replace({'Name':'[A-Za-z]'},0,regex = True) #used as integer
print(replace_regex)