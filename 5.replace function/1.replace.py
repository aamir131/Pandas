import pandas as pd 
df = pd.read_csv("E:\\code\\Pandas\\5.replace function\\Student_data.csv")
print(df)
print()
# this method is used to replace values
# to_replace = old value and 
# value = new value
replace_v = df.replace(to_replace = 'Warren',value = 'Musk') #used as string
print(replace_v)
print()

# this method is used to replace values
# and this method is also used as without parameter

replace_v2 = df.replace('Larry','Musk') #used as string
print(replace_v2)
print()

# this method is used to replace values
# and this method is also used as without parameter

replace_int = df.replace(15000,2021) #used as integer
print(replace_int)
print()

# this method is used to replace lot of values as 1 value using list
# and this method is also used as without parameter

replace_lot = df.replace([101,102,103,104,105,106,107,108,109],5) #used as integer
print(replace_lot)
print()

# this method is used to replace lot of values to different different value using list
# and this method is also used as without parameter

replace_lot_def = df.replace([101,102,103,104,105,106,107,108,109],[1,2,3,4,5,6,7,8,9]) #used as integer
print(replace_lot_def)