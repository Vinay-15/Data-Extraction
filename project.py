from bs4 import BeautifulSoup
import requests
#import datetime as dt

class restaurant:                                                        #Creating a class called restaurant
       def __init__(self,link):                                          #initializing the link and header file
           self.link=link
           self.hdr={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
                     'Accept-Language' : 'en-GB,enl;q=0.5','Referer' : 'https://google.com',
                     'DNT' : '1'}                                        #header used to replicate as a user request rather than python request while accesing websites
           html = requests.get(self.link, headers=self.hdr)
           self.soup = BeautifulSoup(html.text, 'lxml')


       def location(self):                                               #to get the location of the restaurant
              if self.link[12:15]=="swi":
                     locate = self.soup.find_all('span', class_='_3duMr')
                     loc = []
                     for l in locate:
                            loc.append(l.text)                           #getting all elements of the location (Home/India/Bangalore/HSR/)
                     print(loc[-1])                                      #the last element is always the location of the restaurant
              elif self.link[12:15] == "zom":                            #if the given link is of zomato follwing lines are executed
                     location = self.soup.find_all('span', class_='sc-ks3f96-1 gETRUR')
                     loc = []
                     for l in location:
                            loc.append(l.text)                           #getting all elements of the location (Home/India/Bangalore/HSR/)
                     print(loc[4][:len(loc[4]) - 1])


       def ratings(self):                                                #function to get the ratings of the restaurant
              if self.link[12:15] == "swi":
                     Ratings = self.soup.find('div', class_='_1BpLF')
                     rate = []
                     for r in Ratings:
                            rate.append(r.text)                          #getting all the text from the ratings block
                     print(f'Ratings = {rate[-1][:3]}⭐')                #the last element is always the location of the restaurant

              elif self.link[12:15] == "zom":                            #if the given link is of zomato follwing lines are executed
                     Ratings = self.soup.find_all('div', class_='sc-1q7bklc-5 clCBXa')
                     rate = []
                     for r in Ratings:
                            rate.append(r.text)                          #getting all the text from the ratings block
                     print(f'Ratings = {rate[-1][:3]}⭐')


       def sections(self):                                               #to get the categories sections (left panel)
              if self.link[12:15] == "swi":                              #if the given link is of swiggy follwing lines are executed
                     section = self.soup.find_all('h2', class_='M_o7R')  #all the h2 tags are the categories
                     self.s = []
                     for sec in section:
                            self.s.append(sec.text)                      #making a list of all the h2 tags
                     return self.s
              elif self.link[12:15] == "zom":
                     section = self.soup.find_all('p')                   #gettiing all the p tags
                     self.s = []
                     k = []                                              #splitting the category so that it only has the element [Pastas] instead of [Pastas (8)]
                     d = []                                              #making empty lists
                     self.c = []
                     for sec in section:
                            k.append(sec.text)                           #appending all the p tag elements to the list k
                     for i in k:
                            if i != '':                                  #checking if any empty string elements are presnet in the list
                                   d.append(i)                           #removing unwanted data from the list
                     for j in range(len(d)):
                            if d[j][-1] == ')':                          #Recomended (8) #checking if the last element is ')' then appending it to a list
                                   self.s.append(d[j])
                     for p in self.s:
                            j = p.split('(')
                            self.c.append(j[0][:-1])
                     return self.c                                       #Returns the list of all sections


       def check_categories(self,s):                                     #to check if the category is present on the website
              a = input("Enter the categories list with a ',' between consecutive elements:").split(',')  # Enter a list of elements seperated with a ','
              print('-' * 59)                                            #to create a table like view in the output
              print('%-50s %-20s' % ('Categories', 'Status'))
              print('-' * 59)
              for i in a:
                     count = 0
                     for j in s:
                            if i.lower() == j.lower():                   #if i=j then count is incremented with 1 else with 0
                                   count += 1
                            else:
                                   count += 0
                     if (count >= 1):                                    #check if count>=1 then print that the element is present
                            print('%-50s %-20s' %(i, 'Present'))         #%-50s to allot the item name in those 50 spaces
                     else:
                            print('%-50s %-20s' %(i, 'Absent'))
              print('-' * 59)


       def products(self):
              if self.link[12:15] == "swi":                              #if the given link is of swiggy follwing lines are executed
                     products = self.soup.find_all('div', class_='styles_itemName__hLfgz')
                     self.productnames = []
                     for product in products:
                            self.productnames.append(product.text)       #holds all the product names
                     return self.productnames
              elif self.link[12:15] == "zom":                            #if the given link is of swiggy follwing lines are executed
                     products = self.soup.find_all('h4', class_='sc-1s0saks-15 iSmBPS')
                     self.product_names = []
                     for product in products:
                            self.product_names.append(product.text)      #holds all the product names
                     return self.product_names


       def check_products(self,p):
              products = input('Enter the products with a , between them :').split(',')
              print('-' * 59)                                            #to create a table-like output
              print('%-50s %-20s' % ('Products', 'Status'))
              print('-' * 59)
              for product in products:
                     count = 0
                     for ele in p:
                            if product.lower() == ele.lower():           #if product = ele then count is incremented with 1 else with 0
                                   count += 1
                            else:
                                   count += 0
                     if (count >= 1):                                    #check if count>=1 then print that the element is present
                            print('%-50s %-20s' % (product, 'Present'))
                     else:
                            print('%-50s %-20s' % (product, 'Absent'))
              print('-' * 39)


       def menu(self):                                                   #to return a dictionary containing all the sections and products
              if self.link[12:15]=="swi":
                     section = self.soup.find_all('div', class_='_2dS-v')
                     s = []
                     t = []
                     for sec in section:
                            title = sec.find('h2').text                  #to get the section names
                            products = sec.find_all('h3')                #to get all the product names
                            r = []
                            for prod in products:
                                   r.append(prod.text)
                            s.append(title)
                            t.append(r)
                     self.y = dict(zip(s,t))                             #Joining categories and products make them a dictionary
                     return self.y
              elif self.link[12:15] == "zom":
                     n=[]
                     x=[]
                     for i in self.s:                                    #contains the category list from the previous function (sections)
                            k=i.split('(')
                            n.append(int(k[-1][:-1]))
                     l=list(self.product_names)                          #contains the product names from the previous function (products)
                     for j in n:
                         h=[]
                         for k in range(j):
                             h.append(l[0])
                             l.pop(0)
                         x.append(h)
                     self.y = dict(zip(self.c,x))                        #Joining categories and products make them a dictionary
                     return self.y

       def availabilty_score(self):
              inp = input("Enter the section name = ")
              k = int(input("Enter the total number of products of this Category = "))
              avail = (len(self.y[inp])/k)*100
              print(f'Availability Score = {avail}%')



#lnks=['https://www.zomato.com/bangalore/wowffles-hsr-bangalore/order','https://www.zomato.com/bangalore/prowl-foods-by-tiger-shroff-hsr-bangalore/order','https://www.zomato.com/bangalore/the-thickshake-factory-1-hsr-bangalore/order','https://www.zomato.com/bangalore/wowffles-1-bellandur-bangalore/order','https://www.zomato.com/bangalore/prowl-foods-by-tiger-shroff-sarjapur-road-bangalore/order','https://www.zomato.com/bangalore/the-thickshake-factory-sarjapur-road-bangalore/order','https://www.zomato.com/bangalore/wowffles-koramangala-5th-block-bangalore/order','https://www.zomato.com/bangalore/prowl-foods-by-tiger-shroff-koramangala-5th-block-bangalore/order','https://www.zomato.com/bangalore/the-thickshake-factory-koramangala-5th-block-bangalore/order','https://www.zomato.com/bangalore/wowffles-marathahalli-bangalore/order','https://www.zomato.com/bangalore/prowl-foods-by-tiger-shroff-marathahalli-bangalore/order','https://www.zomato.com/bangalore/the-thickshake-factory-brookefield-bangalore/order','https://www.zomato.com/bangalore/wowffles-1-indiranagar-bangalore/order','https://www.zomato.com/bangalore/prowl-foods-by-tiger-shroff-indiranagar-bangalore/order','https://www.zomato.com/bangalore/the-thick-shake-factory-indiranagar-bangalore/order','https://www.zomato.com/bangalore/wowffles-kalyan-nagar-bangalore/order','https://www.zomato.com/bangalore/prowl-foods-by-tiger-shroff-kalyan-nagar-bangalore/order','https://www.zomato.com/bangalore/the-thickshake-factory-kalyan-nagar-bangalore/order']
lnks=input("Enter list of links seperated with a ',' = ").split(',')
for i in range(len(lnks)):

       a=restaurant(lnks[i])
       a.__init__(lnks[i])

       #a.location()                                                      #to find the location
       #a.ratings()                                                       #to find the ratings

       wp_sections=a.sections()                                          #to find the categories from the webpage
       #print(wp_sections)                                                #to print webpage category
       #a.check_categories(wp_sections)                                   #to check if certain category is present

       product=a.products()                                              #to find the products from the webpage
       #print(product)                                                    #to print products of the webpage
       #a.check_products(product)                                         #to check if certain product is present

       menu_dict=a.menu()                                                #to get a dictionary with categories and products
       print(a.y)                                                        #to print the dictionary
       #del a.y['Recommended']                                            #to delete any dictionary elements
       #print(a.y)
       #print(len(a.y['Thick shakes']))                                   #to find the number of elements in any section
       #print(a.y.keys())                                                 #to print all the section names
       #print(a.y.values())                                               #to print all the product names

       a.availabilty_score()                                             #to get the availabilty score of any section

       #time = str(dt.datetime.now()).split()                             #to get the timestamp after executing each
       #print(time[1])
