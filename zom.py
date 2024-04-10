from bs4 import BeautifulSoup
import requests

link='https://www.swiggy.com/restaurants/the-thick-shake-factory-indira-nagar-indiranagar-bangalore-405906' #input('Enter the URL:')
hdr = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
       'Accept-Language' : 'en-GB,enl;q=0.5',
       'Referer' : 'https://google.com',
       'DNT' : '1'}
header = {'User-Agent':'Mozilla/5.0 (Macintosh: Intel Mac OS X 10 11 2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}


html = requests.get(link, headers = hdr)
soup = BeautifulSoup(html.content, 'lxml')
section = soup.find_all('div', class_='_2dS-v')  # all the h2 tags are the categories
s = []
t = []
for sec in section:
    title = sec.find('h2').text
    products=sec.find_all('h3')
    r = []
    for prod in products:
        r.append(prod.text)
    s.append(title)
    t.append(r)

y=dict(zip(s,t))
print(y)
print(len(y['Thick shakes']))
print(y['Thick shakes'])


'''for l in categories:
    loc.append(l.h4)
print(loc[4][:len(loc[4])-1])

Ratings = soup.find_all('div', class_ = 'sc-1q7bklc-5 clCBXa')
rate=[]
for r in Ratings:
    rate.append(r.text)
print(f'Ratings = {rate[-1][:3]}⭐')

sections = soup.find_all('p')
s=[]
for sec in sections:
    s.append(sec.text)
print(s[3:])

#sections = soup.find_all('p')
#s=[]
#k=[]
#for sec in sections:
#    k.append(sec.text)
#k=k[:15]
#for i in range(len(k)):
#    if k[i][-1]==')':
#        s.append(k[i])

#location = soup.find_all('span', class_ = 'sc-ks3f96-1 gETRUR')
#loc=[]
#for l in location:
#    loc.append(l.text)
#print(loc[4][:len(loc[4])-1])

#Ratings = soup.find_all('div', class_ = 'sc-1q7bklc-5 clCBXa')
#rate=[]
#for r in Ratings:
#    rate.append(r.text)
#print(f'Ratings = {rate[-1][:3]}⭐')

#sections = soup.find_all('p')
#s=[]
#for sec in sections:
#    s.append(sec.text)
#print(s[3:])

#sections = soup.find_all('p')
#s=[]
#k=[]
#for sec in sections:
#    k.append(sec.text)
#k=k[:15]
#for i in range(len(k)):
#    if k[i][-1]==')':
#        s.append(k[i])
#print(s)
#locate = soup.find('h4', class_ = 'sc-1s0saks-15 iSmBPS').text
#products = soup.find_all('h4', class_ = 'sc-1s0saks-15 iSmBPS')
#print(products)
#l=[]
#for product in products:
#    l.append(product.text)
#print(l)
 #   product_name = product.find('div', class_ = 'styles_itemName__hLfgz').text
  #  price = product.find('span', class_ = 'rupee').text
   # print(f'Product = {product_name}')
    #print(f'Price = ₹{price}')
'''
