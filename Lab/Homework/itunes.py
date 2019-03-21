from urllib.request import urlopen
from bs4 import BeautifulSoup 
import pyexcel
from collections import OrderedDict

url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode('utf-8')

soup = BeautifulSoup(html_content, "html.parser")
section = soup.find("section", "section chart-grid")

section_list = section.find_all("section-content")
li_list = section.div.ul.find_all("li")
news_list = []
for li in li_list :
    
    h3=li.h3.a
    h4=li.h4.a
    name = h3.string
    artists = h4.string

    news = OrderedDict({
        "name":name,
        "artists" :artists,
    })
    news_list.append(news)
# pyexcel.save_as(records=news_list, dest_file_name="itune.xlsx")
from youtube_dl import YoutubeDL
listsonng = []
for i in news_list:
    ls = i["name"] + "" + i["artists"]
    listsonng.append(ls)

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 10, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(listsonng)

