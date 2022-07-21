import pandas as pd

# create df using list of dict
lst_of_dict = [{"a":1,"b":2},{"a":8,"b":9,"c":5}]
print(lst_of_dict)
print()
lst_of_dict_to_df = pd.DataFrame(lst_of_dict)
print(lst_of_dict_to_df)
print()
# how to creat dictionary of series
dict_of_series = {"a":pd.Series([1,2,3]), "b":pd.Series([4,5,6])}
print(dict_of_series)
print()
# dict of series convert into df
dict_of_series_to_df = pd.DataFrame(dict_of_series)
print(dict_of_series_to_df)