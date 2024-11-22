import requests
import bs4
from colorama import Fore
city=input("plz enter the city:").lower()
response=requests.get(f"https://www.timeanddate.com/weather/iran/{city}/ext")
soup=bs4.BeautifulSoup(response.text,"html.parser")
weather=soup.find_all("div",attrs={"class":"alert__content"})
for i in weather:
    text=i.text
    temp=text.split(".")[0]
    state=text.split(".")[1]
    print(Fore.BLUE+temp)
    print(Fore.LIGHTYELLOW_EX+state.strip())
    print(Fore.RESET)