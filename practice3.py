import requests
import bs4
url="https://takhfifan.com/tehran/restaurants-cafes"
response=requests.get(url)
soup=bs4.BeautifulSoup(response.text,"html.parser")

score=soup.find_all("p",attrs={"class":"rate-badge__rate-value"})
scores=[]
name=soup.find_all("p",attrs={"class":"vendor-card-box__title-text"})
names=[]
for i,j in zip(score,name):
    thescore=i.text.strip()
    scores.append(float(thescore))
    thename=j.text.strip()
    names.append(thename)

max_score = max(scores) 
max_index=scores.index(max_score)
max_name=names[max_index]
print("بیشترین امتیاز:", max_score)
print("نام مربوطه :",max_name)