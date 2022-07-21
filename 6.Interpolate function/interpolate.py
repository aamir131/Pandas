import pandas as pd 
df = pd.read_csv("E:\\code\\Pandas\\6.Interpolate function\\Student_data1.csv")
print(df)
print()
# this method is used to fill NAN value automatically using guess but only numeric value
inter = df.interpolate()
print(inter)
print()
# method default = linear
# this method is used to fill NAN value automatically using guess but only numeric value
inter = df.interpolate(method = 'linear')
print(inter)
print()
