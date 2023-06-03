# Download the HTML of this page then create a python program that lists all the genres and the corresponding user
# counts in a CSV file.

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.goodreads.com/work/shelves/13730452-leviathan-wakes'

response = requests.get(url)
soup = BeautifulSoup(response.content , 'html.parser')
table = soup.find('div',{'class':'left'})

genres = table.find_all('a',{'class':'mediumText'})
genres_list = []
for i in genres:
    genres_list.append(i.text)

cores_num = table.find_all('div',{'class':'smallText'})
cores_num_list = []
for i in cores_num:
    cores_num_list.append(int(i.text.strip().replace(' people','').replace(',','')))

newFile = 'genres_nums.csv'

with open(newFile , 'w' , newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Genres','Corresponding numbers'])

    for genre,count in zip(genres_list,cores_num_list):
        writer.writerow([genre,count])
