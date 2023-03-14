from bs4 import BeautifulSoup
import lxml
import requests
from swiggyfunction import get_soup, get_category
import constant
import pandas as pd
import os

os.mkdir(r'C:\Users\DELL\OneDrive\Desktop\Swiggy')

cities=['kanpur','delhi','bangalore']

swiggy={}

for city in cities:
    name_list=[]
    category_list=[]
    price_list=[]
    time_list=[]
    rating_list=[]
    link_list=[]
    for page in range(1,6):
        url=f'https://www.swiggy.com/city/{city}/top-rated-collection?page={page}'
        soup = get_soup(url)
        #print(soup)

        hotels=soup.find_all('a','_1j_Yo')
        #print(hotel)
        for hotel in hotels:
            link=constant.base_path + hotel['href']
        #print(link)

            name=hotel.find('div','nA6kb').get_text()
        #print(name)

            category=get_category(hotel.find('div','_1gURR').get_text())
         #print(category)

            detail=hotel.find('div','_3Mn31').get_text().split('•')
        #print(detail)

            rating = detail[0]
        #print(rating)

            time=int(detail[1].split(' ')[0])
        #print(time)

            price=int(detail[2].split(' ')[0].replace('₹',''))
        #print(price)

            print(f'''{name},{category},{rating},{time},{price}''')
            name_list.append(name)
            category_list.append(category)
            price_list.append(price)
            time_list.append(time)
            rating_list.append(rating)
            link_list.append(link)

    swiggy['Name']=name_list
    swiggy['Category']=category_list
    swiggy['Price']=price_list
    swiggy['Time']=time_list
    swiggy['Rating']=rating_list
    swiggy['Link']=link_list

    df=pd.DataFrame(swiggy,columns=['Name','Category','Price','Time','Rating','Link'])
    df.to_excel(fr'C:\Users\DELL\OneDrive\Desktop\Swiggy\Swiggy333-{city}.xlsx')


