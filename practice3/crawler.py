import requests
from bs4 import BeautifulSoup
import os

print("-----")
url='https://www.ptt.cc/bbs/Beauty/M.1402765865.A.1EF.html'
headers={'Cookie':'LOGIN_INFO=AFmmF2swRAIgbAfIw4qITtvsvfn8YvQ9w3KCD36F3mHzsKY8vfbbDgMCIG4g0oykeS9anUtXFTsGQhZ673J5Ydp4s6k0XEsfGAjb:QUQ3MjNmeXBRUWpVdU9uUG5EWHRwaDM1LVFWYzZISWxQV1g3SHRFOVg0M1pOeG9lbnhYTFJldTlFOExZYlQ3LXFCLXZGQ29QdU1zc0t5MUdVcG5WLUpFbHctb2c4bV9YVVdSLU9CWllKSHBjWW00MFVqdGdHbktQaUVsOHNwamFpRm94Z2k1eExWTS05NkZfOUpWUFYteTFWRU5kbmk5WmV3; __Secure-3PSID=g.a000pQgkCkClwmn6xLUfgdvgpk-VJqu13AgZKxCELV2k89xwSRTdQu6qs0T4XVMZHtclu-giMwACgYKAVkSARMSFQHGX2MiI057Xvo6LmsSB8r1swmQCRoVAUF8yKpv4wIS6_j4vKSvPRIWYUax0076; __Secure-3PAPISID=KrhDG0MObpBq0K_j/A6hOJlvULITiBNZ-U; YSC=BTuGckIlz_Y; VISITOR_INFO1_LIVE=T_l7fo0vnq4; VISITOR_PRIVACY_METADATA=CgJUVxIEGgAgYA%3D%3D; __Secure-3PSIDTS=sidts-CjIBQT4rXwiH8_uP6oBFQ-2kLzkDx5u6XC_M-RxDdLMowDM1nhAD_5bMEOtjs6Q_xknIqRAA; __Secure-3PSIDCC=AKEyXzW0IZyyh4pfe3L85imqVd3R45FXdsSP3DHrlTjBn-YKFkpTJ3g-sERFrO380xkSGTorBQ'}
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
# print(soup.prettify()) 使資料更加漂亮
spans=soup.find_all("span",class_="article-meta-value") #抓其標題

title=(spans[2].text)
dir_name=f"images/{title}"  #建立一個資料夾，imges 之下 還有一個根據不同tilte而產生的名稱
if not os.path.exists(dir_name): #如果資料夾不存在
  os.makedirs(dir_name) #建立資料夾

#找到圖片網址

links=soup.find_all('a')
for link in links:
  href=link.get("href")
  allow_file_name=['jpg','gif','jpeg','png']
  extension=href.split(".")[-1].lower()
  if extension in allow_file_name:
  # print(extension)
    print(f"file name:{extension}")
    print(f"url:{href}")

  if not href:
    continue
  # print(href)
