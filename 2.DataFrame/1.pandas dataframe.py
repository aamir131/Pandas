import pandas as pd
# how to create empty dataframe
emty = pd.DataFrame()
print(emty)
print()
# how to create dataframe using list
ls = ["w","x","y","z"]  # this is list
print(ls)
print()

df = pd.DataFrame(ls) # here list convert into dataframe
print(df)
print()


list_of_list = [["a","b","c"],["m","n","o"],["x","y","z"]]  # this is nested list
print(list_of_list)

print()

list_to_df = pd.DataFrame(list_of_list) # this method is used to nested list convert into dataframe
print(list_to_df)
print()

dict3 = {"roll":[22,33,25]} # this is dict of list
print(dict3)
print()
dict_to_df = pd.DataFrame(dict3)
print(dict_to_df)
print()
# give both array value same otherwise face to  error
dict_nested = {"roll":[22,33,25],"Class":[4,5,7]} 
print(dict_nested)
print()
nested_dict_to_df = pd.DataFrame(dict_nested)
print(nested_dict_to_df) 
print()
# create df using list of dict
lst_of_dict = [{"a":1,"b":2},{"a":8,"b":9}]
print(lst_of_dict)
print()
lst_of_dict_to_df = pd.DataFrame(lst_of_dict)
print(lst_of_dict_to_df)