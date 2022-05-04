import requests
from bs4 import BeautifulSoup

url = "https://www.travel.taipei/zh-tw/statistical-bulletin/number-of-visitors"

start_year = 2022
end_year = 2022
start_month = 1
end_month = 1
time_range = 1

params = {'start-year':start_year,
          'end-year':end_year,
          'start-month':start_month,
          'end-month':end_month,
          'range':time_range}

response = requests.get(url,params=params)
soup = BeautifulSoup(response.text,"html.parser")
data_div = soup.find('ol',class_='statistic-chart-list')

spots = data_div.select('.item')
for spot in spots:
    place = spot.select_one('.name').text
    visit = spot.select_one('.info').get('data-num').replace(',','')
    print(place,visit)

