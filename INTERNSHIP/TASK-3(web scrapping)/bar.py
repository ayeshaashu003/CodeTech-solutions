import requests
from bs4 import BeautifulSoup

url= "https://www.thehindu.com/"

r= requests.get(url,headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
)
soup=BeautifulSoup(r.text,'lxml')

with open("C:\INTERNSHIP\TASK-3(web scrapping)\Latest_news.txt", "w", encoding="utf-8") as file:
    for latest in soup.find(class_="timeline"):
        print(latest.get_text())
        file.write(latest.get_text())

