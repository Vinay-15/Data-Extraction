from tkinter import *
from bs4 import BeautifulSoup
import requests

app = Tk()
app.geometry('1000x600')
app.title("TTSF Cloud One")
msg=Label(app,text="TTSF Cloud One",background="teal",foreground="Orange", font=("Times",20))
msg.grid(row=0,column=0,padx=25,pady=5,columnspan=6)
app['background']="teal"
links=Label(app,text="Enter the link/links (separated with a ',') : ",background="teal",foreground="Black", font=("Times",14))
linksE=Entry(app,width=45,background="grey",foreground="black")

links.grid(row=2,column=0,padx=25,pady=5)
linksE.grid(row=2,column=1,padx=50,pady=15)


def location():                                                #to get the location of the restaurants
       lnk=linksE.get()
       html = requests.get(lnk, headers=hdr)
       soup = BeautifulSoup(html.text, 'lxml')
       if lnk.get()[12:15]=="swi":                                     #if the given link is of swiggy follwing lines are executed
              locate = soup.find_all('span', class_='_3duMr')
              loc = []
              for l in locate:
                     p = Label(app, text=l[-1])                          #getting all elements of the location (Home/India/Bangalore/HSR/)
                     p.grid(row=4,column=1,padx=50,pady=15)
def pri():
       lin=linksE.get()
       p = Label(app,text=lin)
       p.grid(row=4, column=1, padx=50, pady=15)

hdr = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
       'Accept-Language' : 'en-GB,enl;q=0.5',
       'Referer' : 'https://google.com',
       'DNT' : '1'}                                              #header used to replicate as a user request rather than python request while accesing websites


#locaton(link)                                                    #to find the location
#ratings(link)                                                    #to find the ratings
#wp_category=sections(link)                                       #to find the categories from the webpage
#print(wp_category)                                               #to print webpage category
#check(wp_category)                                               #to check if certain category is present
#products(link)



location=Button(app,text="location",command=pri() ,background='grey'e)
location.grid(row=3,column=1,padx=25,pady=5,columnspan=2)

app.mainloop()