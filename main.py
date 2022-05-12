from bs4 import BeautifulSoup
import requests

link=input('Enter the URL:')
html = requests.get(link).text
soup = BeautifulSoup(html, 'lxml')
locate = soup.find('div', class_ = '_2p-Tc').text
<<<<<<< HEAD
products = soup.find_all('div', class_ ='_2wg_t')
for product in products:
=======
<<<<<<< HEAD
products = soup.find_all('div', class_ ='_2wg_t')
for product in products:
=======
<<<<<<< HEAD
products = soup.find_all('div', class_ ='_2wg_t')
for product in products:
=======
products = soup.find_all('div', class_ ='styles_itemName__hLfgz')
product_name=[]
for product in products:
<<<<<<< HEAD
>>>>>>> 660f2e0 (Initial commit)
>>>>>>> 95b0e0f (Initial commit)
>>>>>>> fa30d79 (Initial commit)
    product_name = product.find('div', class_ = 'styles_itemName__hLfgz').text
    price = product.find('span', class_ = 'rupee').text
    print(f'Product = {product_name}')
    print(f'Price = ₹{price}')
    
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
    #product_name = product.find('div', class_ = 'styles_itemName__hLfgz').text
    product_name.append(product.text)
    #price = product.find('span', class_ = 'rupee').text
    #print(f'Product = {product_name}')
    #print(f'Price = ₹{price}')
print(product_name)
>>>>>>> 1e0f363 (fourth)
>>>>>>> 660f2e0 (Initial commit)
>>>>>>> 95b0e0f (Initial commit)
>>>>>>> fa30d79 (Initial commit)
