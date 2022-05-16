from bs4 import BeautifulSoup
import requests
import datetime as dt


class restaurant:
    def __init__(self):
        self.link = input('Enter the URL:')
        self.hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
                    'Accept-Language': 'en-GB,enl;q=0.5', 'Referer': 'https://google.com',
                    'DNT': '1'}                                     #header used to replicate as a user request rather than python request while accesing websites
        html = requests.get(self.link, headers=self.hdr)
        self.soup = BeautifulSoup(html.text, 'lxml')

    def location(self):
        if self.link[12:15] == "swi":
            locate = self.soup.find_all('span', class_='_3duMr')
            loc = []
            for l in locate:
                loc.append(l.text)                                  #getting all elements of the location (Home/India/Bangalore/HSR/)
            print(loc[-1])                                          #the last element is always the location of the restaurant
        elif self.link[12:15] == "zom":                             #if the given link is of zomato follwing lines are executed
            location = self.soup.find_all('span', class_='sc-ks3f96-1 gETRUR')
            loc = []
            for l in location:
                loc.append(l.text)                                  #getting all elements of the location (Home/India/Bangalore/HSR/)
            print(loc[4][:len(loc[4]) - 1])

    def ratings(self):
        if self.link[12:15] == "swi":
            Ratings = self.soup.find('div', class_='_1BpLF')
            rate = []
            for r in Ratings:
                rate.append(r.text)                                 #getting all the text from the ratings block
            print(f'Ratings = {rate[-1][:3]}⭐')                    #the last element is always the location of the restaurant

        elif self.link[12:15] == "zom":                             #if the given link is of zomato follwing lines are executed
            Ratings = self.soup.find_all('div', class_='sc-1q7bklc-5 clCBXa')
            rate = []
            for r in Ratings:
                rate.append(r.text)                                 #getting all the text from the ratings block
            print(f'Ratings = {rate[-1][:3]}⭐')

    def sections(self):                                             #to get the categories sections (left panel)
        if self.link[12:15] == "swi":                               #if the given link is of swiggy follwing lines are executed
            section = self.soup.find_all('h2', class_='M_o7R')      #all the h2 tags are the categories
            s = []
            for sec in section:
                s.append(sec.text)                                  #making a list of all the h2 tags
            return s
        elif self.link[12:15] == "zom":
            section = self.soup.find_all('p')                       #gettiing all the p tags
            s = []
            k = []                                                  #splitting the category so that it only has the element [Pastas] instead of [Pastas (8)]
            d = []                                                  #making empty lists
            c = []
            for sec in section:
                k.append(sec.text)                                  #appending all the p tag elements to the list k
            for i in k:
                if i != '':                                         #checking if any empty string elements are presnet in the list
                    d.append(i)                                     #removing unwanted data from the list
            for j in range(len(d)):
                if d[j][-1] == ')':                                 #Recomended (8) #checking if the last element is ')' then appending it to a list
                    s.append(d[j])
            for p in s:
                j = p.split('(')
                c.append(j[0])
            return c

    def check_categories(self, s):                                  #to check if the category is present on the website
        cat = []
        for i in s:
            if i[
                -1] == ' ':                                         #zomato links categories are printed as 'Pastas ' <--to remove the last element and append it
                cat.append(i.lower()[:-1])
            else:
                cat.append(
                    i.lower())                                      #swiggy link categories are printed as 'Pastas' without any extra spaces
        a = input("Enter the categories list with a ',' between consecutive elements:").split(
            ',')                                                    #Enter a list of elements seperated with a ','
        for i in a:
            count = 0
            for j in cat:
                if i.lower() == j:                                  #if i=j then count is incremented with 1 else with 0
                    count += 1
                else:
                    count += 0
            if (count >= 1):                                        #check if count>=1 then print that the element is present
                print(f'{i.capitalize()} is present')
            else:
                print(f'{i.capitalize()} is absent')


    def products(self):
        if self.link[12:15] == "swi":                              #if the given link is of swiggy follwing lines are executed
            products = self.soup.find_all('div', class_='styles_itemName__hLfgz')
            product_names = []
            for product in products:
                product_names.append(product.text)                 #holds all the product names
            return (product_names)
        elif self.link[12:15] == "zom":                            #if the given link is of swiggy follwing lines are executed
            products = self.soup.find_all('h4', class_='sc-1s0saks-15 iSmBPS')
            product_names = []
            for product in products:
                product_names.append(product.text)                 #holds all the product names
            return product_names

    def check_products(self, p):
        products = input('Enter the products with a , between them :').split(',')
        for product in products:
            count = 0
            for ele in p:
                if product.lower() == ele.lower():                 #if product=ele then count is incremented with 1 else with 0
                    count += 1
                else:
                    count += 0
            if count >= 1:                                         #check if count>=1 then print that the element is present
                print(f'{product} is present')
            else:
                print(f'{product} is absent')


a = restaurant()
a.location()                                                       #to find the location
a.ratings()                                                        #to find the ratings

wp_sections = a.sections()                                         #to find the categories from the webpage
print(wp_sections)                                                 #to print webpage category
#a.check_categories(wp_sections)                                    #to check if certain category is present

product = a.products()                                             #to find the products from the webpage
print(product)                                                     #to print products of the webpage
#a.check_products(product)                                          #to check if certain product is present
a = str(dt.datetime.now()).split()
print(a[1])