import requests
from bs4 import BeautifulSoup

site = input('Digite a empresa:')
page = requests.get('https://downdetector.com/status/'+ site)

soup = BeautifulSoup(page.content, 'lxml')
if soup.find_all(class_='alert mt-2 alert-success'):
    print('OK')
elif soup.find_all(class_='alert mt-2 alert-warning'):
    print('Danger')
else:
    print('Down')