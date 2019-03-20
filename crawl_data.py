from urllib.request import urlopen
from bs4 import BeautifulSoup 
import pyexcel
from collections import OrderedDict

# 1. Create connection
url = "https://dantri.com.vn"
conn = urlopen(url)

# 1.1 Download page
raw_data = conn.read()
html_content = raw_data.decode('utf-8')

with open("dantri.html", "wb") as f:
    f.write(raw_data)
# print(html_content)
# # 2. Find ROI
# soup = BeautifulSoup(html_content, "html.parser")
# ul = soup.find("ul", "ul1 ulnew")
# # print(a.prettify())
#     # print("*" *50)
# # print(ul.prettify())
# # 3. Extract ROI
# li_list = ul.find_all("li")
# news_list = []
# for i in range(len(li_list)):
#     li = li_list[i]
#     h4 = li.h4
#     a= h4.a 

#     title = a.string 
#     link = url + a["href"] 

#     news = OrderedDict({
#         "title":title.lstrip().rstrip(),
#         "link" :link,
#     })
#     news_list.append(news)

# # 4. Save data
# pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")
