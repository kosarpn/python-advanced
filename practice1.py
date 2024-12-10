# -*- coding: utf-8 -*-
import requests
import bs4
import time
url="https://tv.filmnet.ir/"
response=requests.get(url)
soup=bs4.BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())
title=soup.find_all("p",attrs={"class":"etkpj6e6 css-1gn0tgp eg0dt7k0"})
# whichone=soup.find_all("h1",attrs={"class:css-lpmk21 eg0dt7k0"})


for i in title:
    name=i.text
    print(name)

