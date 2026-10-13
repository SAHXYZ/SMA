import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")
books = []

for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p",class_="price_color").text
    availability = book.find("p",class_="instock availability").text
    books.append({
        "Title" : title,
        "Price" : price,
        "Availability" : availability
    })
df = pd.DataFrame(books)
print(df)
df.to_csv("Practical 4/books_data.csv", index=False)
print("\nData Successfully Saved Into books_data.csv")

