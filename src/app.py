__author__ = "miorsufian"

import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.johnlewis.com/john-lewis-wade-office-chair-black/p447855")

content = request.content
print(content)
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
print(element.text.strip())
string_price = element.text.strip() #£99.00

price_without_symbol = string_price[1:] #£99.00
price = float(price_without_symbol)

if price < 200:
    print("You should buy the chair!")
    print("The current price is {}".format(price))
else:
    print("Do not buy, it's too expensive")
