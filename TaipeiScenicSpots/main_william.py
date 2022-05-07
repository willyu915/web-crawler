import requests
from bs4 import BeautifulSoup

def visitors_info_list(start_year,end_year,time_range,start_month=1,end_month=1):
    """
    input:
      integer: start_year,end_year,start_month,end_month,time_range
      string: time_range (year or spot)
    output:
      list: new_visitor_list
    """
    year_sw = True
    if time_range=='year':
        time_range=0
    elif time_range=='spot':
        time_range=1
        year_sw = False
    url = "https://www.travel.taipei/zh-tw/statistical-bulletin/number-of-visitors"
    params = {'start-year':start_year,
            'end-year':end_year,
            'start-month':start_month,
            'end-month':end_month,
            'range':time_range}

    response = requests.get(url,params=params)
    soup = BeautifulSoup(response.text,"html.parser")
    data_div = soup.find('ol',class_='statistic-chart-list')

    spots = data_div.select('.item')

    new_visitor_list = []
    for spot in spots:
        place = spot.select_one('.name').text
        visit = spot.select_one('.info').get('data-num').replace(',','')
        new_visitor_list.append([place,visit])
    return new_visitor_list,year_sw


if __name__ == "__main__":
    start_year = 2021
    end_year = 2022
    start_month = 10
    end_month = 1
    time_range = 1
    new_visitor_info_list = visitors_info_list(start_year,end_year,start_month,end_month,time_range)
    print(new_visitor_info_list)