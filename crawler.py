import requests
from bs4 import BeautifulSoup
import json

url="https://www.ptt.cc/bbs/Japan_Travel/index.html"
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
article=soup.find_all("div", class_="r-ent")
data_list=[]
for x in article:
  data={}
  title=x.find("div",class_="title")
  if title and title.a:
    title=title.a.text
  else:
    title="沒有標題" 
  data["標題"]=title

  popular=x.find("div",class_="nrec")
  if popular and popular.span:
    popular=popular.span.text
  else:
    popular="無法顯示"
  data["人氣"]=popular


  date=x.find("div",class_="date")
  if date:
    date=date.text
  else:
    date="沒有日期"

  data["日期"]=date
  
  data_list.append(data)

print(data_list)

  # print(f"標題:{title} 人氣:{popular} 日期:{date}")