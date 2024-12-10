import requests
import bs4
import time
url="https://karnameh.com/car-price"
response=requests.get(url)
soup=bs4.BeautifulSoup(response.text,"html.parser")
name=soup.find_all("p",attrs={"class":"MuiTypography-root MuiTypography-body1 muirtl-iy5bpq"})
price=soup.find_all("p",attrs={"class":"MuiTypography-root MuiTypography-body1 muirtl-22intj"})
for i,j in zip(name,price):
    thename=i.text
    leprix=j.text
    print(f"the name:{thename},price:{leprix}")
