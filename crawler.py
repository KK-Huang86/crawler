import requests
from bs4 import BeautifulSoup

url="https://www.ptt.cc/bbs/Japan_Travel/index.html"
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
article=soup.find_all("div", class_="r-ent")
for x in article:
  title=x.find("div",class_="title")
  if title and title.a:
    title=title.a.text
  else:
    title="沒有標題" 


  popular=x.find("div",class_="nrec")
  if popular and popular.span:
    popular=popular.span.text
  else:
    popular="無法顯示"

  date=x.find("div",class_="date")
  if date:
    date=date.text
  else:
    date="沒有日期"

  print(f"標題:{title} 人氣:{popular} 日期:{date}")