import pandas as pd

from main_william import visitors_info_list


data = visitors_info_list(2019,2021,'spot',11,2)

spot_list = []
number_list = []
for d in data:
    spot_list.append(d[0])
    number_list.append(d[1])



list1 = spot_list
list2 = number_list
col1 = "location"
col2 = "number of visitors"
data = pd.DataFrame({col1:list1,col2:list2})
data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)