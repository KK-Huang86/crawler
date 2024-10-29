import requests
from bs4 import BeautifulSoup
import pandas

url="https://www.ptt.cc/bbs/Japan_Travel/index.html"
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser") #"html.parser html解析器"
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
  
  data_list.append(data) #將抓回來的資料寫進data_list

result=pandas.DataFrame(data_list)
result.to_excel("PTT_Japan_Travel.xls",index=False,engine="openpyxl") #將result轉成excel,第一個空格為檔案名稱，以及開啟的方式

print("資料已經成功轉換")
print(data_list)
