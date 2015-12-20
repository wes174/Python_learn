import requests
from bs4 import BeautifulSoup

def link_spider(max_p):
    p = 2
    while p <= max_p:
        url = 'http://www.topit.me/?p=' + str(p)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a',{'target':'_blank'}):
            href = link.get('href')
            print(href)
        p += 1
link_spider(2)
