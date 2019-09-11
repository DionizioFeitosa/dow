import requests
from bs4 import BeautifulSoup

site = input('Digite a empresa:')
page = requests.get('https://downdetector.com/status/'+ site)

soup = BeautifulSoup(page.content, 'lxml')
if soup.find_all(class_='alert mt-2 alert-success'):
    print('Sem Problemas')
elif soup.find_all(class_='alert mt-2 alert-warning'):
    print('Passando por Problema')
else:
    print('Perigo')


