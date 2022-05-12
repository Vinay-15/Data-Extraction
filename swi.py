from bs4 import BeautifulSoup
import requests

link=input('Enter the URL:')
hdr = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
       'Accept-Language' : 'en-GB,enl;q=0.5',
       'Referer' : 'https://google.com',
       'DNT' : '1'}

html = requests.get(link, headers=hdr)
soup = BeautifulSoup(html.text, 'lxml')
locate = soup.find_all('span', class_ = '_3duMr')
loc=[]
for l in locate:
    loc.append(l.text)
print(loc[-1])

Ratings = soup.find('div', class_ = '_1BpLF')
rate=[]
for r in Ratings:
    rate.append(r.text)
print(f'Ratings = {rate[-1][:3]}⭐')

sections = soup.find_all('h2', class_ ='M_o7R')
s=[]
for sec in sections:
    s.append(sec.text)
print(s)