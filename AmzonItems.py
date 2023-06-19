import bs4 as bs
import urllib.request

url = 'https://www.amazon.de/s?k=ipjone14pro+max&crid=C7AHBLBK4D7S&sprefix=ipj%2Caps%2C108&ref=nb_sb_ss_ts-doa-p_1_3'
source = urllib.request.urlopen(f'{url}').read()
soup = bs.BeautifulSoup(source, 'lxml')
name = soup.find_all('span', {'class': 'a-size-medium'})
price = soup.find_all('span', {'class': 'a-price-whole'})

newDict = {}
for k, v in list(zip(name, price)):
    newDict[k.string] = v.string

for k, v in newDict.items():
    print(k,v)
