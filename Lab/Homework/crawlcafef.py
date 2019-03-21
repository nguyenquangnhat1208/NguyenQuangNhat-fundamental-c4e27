from urllib.request import urlopen
from bs4 import BeautifulSoup 
import pyexcel
from collections import OrderedDict

# 1. Create connection
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

# 1.1 Download page
raw_data = conn.read()
html_content = raw_data.decode('utf-8')
# with open("cafef.html", "wb") as f:
#     f.write(raw_data)
soup = BeautifulSoup(html_content, "html.parser")
id = soup.find("table",id="tableContent" )
tr_list = id.find_all("tr")
news_list = []
for tr in tr_list :
    td_list = tr.find_all("td")
    content = {}
    for i in range(len(td_list)):
        if td_list[i].string != None:
            if i == 0:
                content["danh mục"] = td_list[i].string.strip()
            elif i ==1:
                content["quý 4-2016"] = td_list[i].string.strip()     
            elif i == 2:
                content["quý 1-2017"] =td_list[i].string.strip()
            elif i == 3:
                content["quý 2-2017"] =td_list[i].string.strip()
            elif i==4:
                content["quý 3-2017"] = td_list[i].string.strip()
    if content != {}:
        news_list.append(content)

# print(news_list)
pyexcel.save_as(records=news_list, dest_file_name="cafef.xlsx")