
import requests
from bs4 import BeautifulSoup


def book_info_list(page_url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    # price
    price_total = soup.select(" .table-searchlist .list-nav > li")

    price_filter_list = []

    for price_block in price_total:
        price_list = price_block.select('strong')
        if len(price_list)==2:
            price_filter_list.append(price_list[1].text)
        elif len(price_list) == 1:
            price_filter_list.append(price_list[0].text)
        else:
            print("error")


    # img link
    img_total = soup.select(".table-searchlist .box_1 img")
    image_list = []
    for img in img_total:
        image_list.append(img.get('data-src').split("?")[1].split("&")[0][2:])

    # book name
    book_name_total = soup.select("tr > td:nth-child(3) > h4 > a")
    book_name_list = []
    for book_name in book_name_total:
        book_name_list.append(book_name.text)


    #author and publisher
    author_list_total = soup.select("tr > td:nth-child(3) > ul:nth-child(2) > li")
    author_list = []
    for i in author_list_total:
        temp_a_list = i.select("a")
        temp_publish_list = []
        for j in temp_a_list:
            temp_publish_list.append(j.text)
        author_list.append(temp_publish_list)

    #publish date
    publish_date_list = []
    for i in author_list_total:
        publish_date_list.append(i.text.split(':')[1])

    #book link
    book_link_total = soup.select("tr > td:nth-child(3) > h4 > a")
    book_link_list = []
    for i in book_link_total:
        book_link_list.append("https:" + i.get("href"))

    out_data = []
    for i in range(24):
        all_author_str = ",".join(author_list[i][:-1])
        publish_date = publish_date_list[i].replace(' ','')
        out_data.append([book_name_list[i], \
                        all_author_str, \
                        price_filter_list[i], \
                        image_list[i], \
                        author_list[i][-1], \
                        publish_date,\
                        book_link_list[i]])
    # print(out_data[1])

    return out_data

page_num = 3
url = "https://search.books.com.tw/search/query/cat/all/sort/1/v/0/spell/3/ms2/ms2_1/page/"+ str(page_num) +"/key/python+%E5%85%A5%E9%96%80"

new_book_info_list = book_info_list(url)


file = open("output.txt",'w')
for k in new_book_info_list:
    file.write(str(k)+'\n')
file.close()