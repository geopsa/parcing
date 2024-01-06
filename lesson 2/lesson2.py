import requests
from bs4 import BeautifulSoup


### сохранить страницу

#url = 'https://health-diet.ru/calorie'

#headers = {
#    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Avast/120.0.0.0',
#}

#req = requests.get(url, headers=headers)
#src = req.text
#print(src)

#with open('index.html', 'w') as file:    #создать файл, написать файл
#    file.write(src)

###

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_products_hrefs = soup.find_all(class_='mzr-user-select-none mzr-tree mzr-tree-with-padding mzr-tree-with--top-radius mzr-tree-with--min-height')

for item in all_products_hrefs:
    #print(all_products_hrefs)
    item_text = item.text
    item_href = item.get('href')