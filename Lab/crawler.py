# import requests
# url = 'https://dantri.com.vn/suc-khoe.htm'
# response = requests.get(url)
# print(response.content.decode())
import requests
from bs4 import BeautifulSoup

url = 'https://dantri.com.vn/suc-khoe.htm'

response = requests.get(url)

html = response.content.decode('utf-8')

soup = BeautifulSoup(html,'html.parser')

all_div = soup.find_all('div',{'data-boxtype':'timelineposition'})
arr=[]
for v in all_div:
    arr.append({"title":v.div.h2.a.string,"image":v.a.img['src']})
    # print(v.div.h2.a.string)
    # print(v.a.img['src'])
    # print(v.div.div.text)
print(arr)