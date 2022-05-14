from bs4 import BeautifulSoup
import requests

def locaton(lnk):                                                #to get the location of the restaurants
       html = requests.get(lnk, headers=hdr)
       soup = BeautifulSoup(html.text, 'lxml')
       if lnk[12:15]=="swi":                                     #if the given link is of swiggy follwing lines are executed
              locate = soup.find_all('span', class_='_3duMr')
              loc = []
              for l in locate:
                     loc.append(l.text)                          #getting all elements of the location (Home/India/Bangalore/HSR/)
              print(loc[-1])                                     #the last element is always the location of the restaurant
       elif lnk[12:15]=="zom":                                   #if the given link is of zomato follwing lines are executed
              location = soup.find_all('span', class_='sc-ks3f96-1 gETRUR')
              loc = []
              for l in location:
                     loc.append(l.text)                          #getting all elements of the location (Home/India/Bangalore/HSR/)
              print(loc[4][:len(loc[4]) - 1])                    #the 4th element is the location (in the format:HSR/) indexing to strip the last element


def ratings(lnk):                                                #to get the ratings of the Restaurants
       html = requests.get(lnk, headers=hdr)
       soup = BeautifulSoup(html.text, 'lxml')
       if lnk[12:15] == "swi":                                   #if the link is swiggy following lines are to be executed
              Ratings = soup.find('div', class_='_1BpLF')
              rate = []
              for r in Ratings:
                     rate.append(r.text)                         #getting all the text from the ratings block
              print(f'Ratings = {rate[-1][:3]}⭐')               #the last element contains a string with the rate being the starting 3 elements
       elif lnk[12:15] == "zom":                                 #if the link is zomato following lines are to be executed
              Ratings = soup.find_all('div', class_='sc-1q7bklc-5 clCBXa')
              rate = []
              for r in Ratings:
                     rate.append(r.text)                         #getting all the text from the ratings block
              print(f'Ratings = {rate[-1][:3]}⭐')               #the last element contains a string with the rate being the starting 3 elements


def sections(lnk):                                               #to get the categories sections (left panel)
       html = requests.get(lnk, headers=hdr)
       soup = BeautifulSoup(html.text, 'lxml')
       if lnk[12:15] == "swi":                                   #if the given link is of swiggy follwing lines are executed
              section = soup.find_all('h2', class_='M_o7R')      #all the h2 tags are the categories
              s = []
              for sec in section:
                     s.append(sec.text)                          #making a list of all the h2 tags
              return s
       elif lnk[12:15] == "zom":
              section = soup.find_all('p')                       #gettiing all the p tags
              s = []
              k = []
              c = []                                             #making empty lists
              d = []
              for sec in section:
                     k.append(sec.text)                          #appending all the p tag elements to the list k
              for i in k:
                     if i!='':                                   #checking if any empty string elements are presnet in the list
                            d.append(i)                          #removing unwanted data from the list
              for i in range(len(d)):
                     if d[i][-1] == ')':                         #Recomended (8) #checking if the last element is ')' then appending it to a list
                            s.append(d[i])
              for p in s:
                     j = p.split('(')                            #splitting the category so that it only has the element [Pastas] instead of [Pastas (8)]
                     c.append(j[0])
              return c


def check_categories(s):                                         #to check if the category is present on the website
       cat=[]
       for i in s:
              if i[-1]==' ':                                     #zomato links categories are printed as 'Pastas ' <--to remove the last element and append it
                     cat.append(i.lower()[:-1])
              else:
                     cat.append(i.lower())                       #swiggy link categories are printed as 'Pastas' without any extra spaces
       a=input("Enter the categories list with a ',' between consecutive elements:").split(',')  #Enter a list of elements seperated with a ','
       for i in a:
              count = 0
              for j in cat:
                     if i.lower()==j:                            #if i=j then count is incremented with 1 else with 0
                            count+=1
                     else:
                            count+=0
              if(count>=1):                                      #check if count>=1 then print that the element is present
                     print(f'{i.capitalize()} is present')
              else:
                     print(f'{i.capitalize()} is absent')


def products(lnk):
       html = requests.get(lnk, headers=hdr)
       soup = BeautifulSoup(html.text, 'lxml')
       if lnk[12:15] == "swi":                                   #if the given link is of swiggy follwing lines are executed
              products = soup.find_all('div', class_='styles_itemName__hLfgz')
              product_names = []
              for product in products:
                     product_names.append(product.text)          #holds all the product names
              return (product_names)
       elif lnk[12:15] == "zom":                                 #if the given link is of swiggy follwing lines are executed
              products = soup.find_all('h4', class_='sc-1s0saks-15 iSmBPS')
              product_names = []
              for product in products:
                     product_names.append(product.text)           #holds all the product names
              return product_names


def check_products(p):
       products = input('Enter the products with a , between them :').split(',')
       for product in products:
              count=0
              for ele in p:
                     if product.lower() == ele.lower():           #if product=ele then count is incremented with 1 else with 0
                            count+=1
                     else:
                            count+=0
              if count>=1:                                        #check if count>=1 then print that the element is present
                     print(f'{product} is present')
              else:
                     print(f'{product} is absent')


link=input('Enter the URL:')
hdr = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
       'Accept-Language' : 'en-GB,enl;q=0.5',
       'Referer' : 'https://google.com',
       'DNT' : '1'}                                              #header used to replicate as a user request rather than python request while accesing websites


#locaton(link)                                                    #to find the location
#ratings(link)                                                    #to find the ratings
#wp_category=sections(link)                                       #to find the categories from the webpage
#print(wp_category)                                               #to print webpage category
#check_categories(wp_category)                                    #to check if certain category is present
p = products(link)                                               #to get the products of a restaurant
print(p)
check_products(p)                                                #to check if a given list of products are present on the webpage
