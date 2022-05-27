import pandas as pd

from main_william import visitors_info_list
    
year_or_spot_list = []
number_list = []
month_list = []
year_list = []

for year in range (2019,2023):
    for month in range(1,13):
        if not(year == 2022 and 4<= month):
            data,year_sw = visitors_info_list(year,year,'spot',month,month)

            for d in data:
                year_or_spot_list.append(d[0])
                number_list.append(d[1])
                month_list.append(month)
                year_list.append(year)

    
if year_sw:
    col1 = "year"
else:
    col1 = "location"
col2 = "number of visitors"
col3 = "month"
col4 = "year"
data = pd.DataFrame({col1:year_or_spot_list,col2:number_list,col3:month_list,col4:year_list})
data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)