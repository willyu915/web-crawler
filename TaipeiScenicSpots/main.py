import pandas as pd

from main_william import visitors_info_list


for year in range (2019,2023):
    for month in range(1,13):
        data,year_sw = visitors_info_list(year,year,'spot',month,month)

        year_or_spot_list = []
        number_list = []
        for d in data:
            year_or_spot_list.append(d[0])
            number_list.append(d[1])

        list1 = year_or_spot_list
        list2 = number_list
        if year_sw:
            col1 = "year"
        else:
            col1 = "location"
        col2 = "number of visitors"
        data = pd.DataFrame({col1:list1,col2:list2})
        data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)