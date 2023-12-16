# Importing important libraries for Web scrapping
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Content of the Page
books = []
for i in range(1, 2):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    res = requests.get(url)
    resp = res.content
    # print(resp)

    soup = BeautifulSoup(resp, "html.parser")
    # print(soup)

    # Finding Ol Tag

    ol = soup.find('ol')
    articles = ol.find_all('article', class_="product_pod")
    # print(articles)

    for art in articles:
        image = art.find("img")
        title = image.attrs['alt']
        img = image.attrs['src'][3:]

        img = f'https://books.toscrape.com/{img}'
        # print(title)

        star = art.find('p')
        star = star['class'][1]
        # print(star)

        price = art.find('p', class_='price_color').text
        price = float(price[1:])
        # print(price)

        books.append([title, price, star, img])
        # print(books)

df = pd.DataFrame(books, columns=['Title', 'Price', 'StarRating','Image'])
df.to_csv("Books1.csv")
