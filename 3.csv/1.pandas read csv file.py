import pandas as pd
# always here type \\ double slash otherwise give error
# this method is used to import csv file and this is 2d(rows and columns) data structure also called as dataframe
# import csv file as dataframe
stu_data = pd.read_csv("E:\\code\\Pandas\\3.csv\\Student_data.csv")
print(stu_data)
print()
# always here type \\ double slash otherwise give error
# this method is used to import csv file and this is 1d data structure also called as Series
# import csv file as series
topreach_data = pd.read_csv("E:\\code\\Pandas\\3.csv\\Top Reachest.csv")
print(topreach_data)
print()
