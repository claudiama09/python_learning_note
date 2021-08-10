import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

print(soup.select('body > div '))

title_prices = []

for article in soup.find_all('article'):
    title = article.h3.a['title']
    price = article.find('p', class_='price_color')
    title_prices.append({title: float(price.text.lstrip('£'))})

# print(soup.find_all('a'))