from pandas.io import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

products_list = []

base_url = 'https://lista.mercadolivre.com.br/'
search_term = input("Qual produto deseja buscar? ")

response = requests.get(base_url + search_term)

site = BeautifulSoup(response.text, 'html.parser')

products = site.findAll('li', attrs={'class':'ui-search-layout__item'})

for product in products:
    item_title = product.find('h2', attrs={'class': 'ui-search-item__title'})
    item_link = product.find('a', attrs={'class': 'ui-search-link'})

    symbol_moeda = product.find('span', attrs={'class': 'price-tag-symbol'})
    real = product.find('span', attrs={'class': 'price-tag-fraction'})
    centavo = product.find('span', attrs={'class': 'price-tag-cents'})

    if(centavo):
        # print('Preço do produto: ', symbol_moeda.text + real.text +','+ centavo)
        products_list.append([item_title.text, item_link['href'], symbol_moeda.text, real.text, centavo.text])
    else:
        # print('Preço do produto: ', symbol_moeda.text + real.text)
        products_list.append([item_title.text, item_link['href'], symbol_moeda.text, real.text, ''])

productsData = pd.DataFrame(products_list, columns=['Título', 'Link', 'Moeda', 'Fracionado', 'Centavos'])

with open('products.json', 'w', encoding='utf-8') as jp:
    result = productsData.to_json(orient="records")
    parsed = json.loads(result)
    js = json.dumps(parsed, indent=4)
    jp.write(js)