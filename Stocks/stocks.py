import csv

def stock_order(a,b,s):                                      #This function tells you the number of ingredients required to make the Product
    print(f"Ingredients needed to make {b} {a}'s are:")
    print('-' * 26)
    print("%-17s %-9s" %('Product','Quantity'))
    print('-' * 26)
    for product in s:
        if product[0] == a:
            for j in range(1,len(product)):
                l = product[j].split('-')                    #Splitting the element as the first half consists of quantity of the element
                quantity = (int(l[0]))*b                     #Quantity is the usually first element and converting it into integer
                prod = l[1]                                  #Product is usually the next element
                print("%-20s %-4s" %(prod,quantity))
    print('-' * 26)


with open ('stocks.csv','r') as file:                        #Opens the file from the same directory
    csv_r = csv.reader(file)                                 #reads the file
    print("List of Items:")
    s=[]
    for k in csv_r:
        s.append(k)
        print(k[0], end=', ')                                #Printing all the Products whose ingredients are present in the csv file

a = input('\nEnter the product : ')
b = int(input('Enter the quantity:'))
stock_order(a,b,s)                                           #To get the number of igredients required for large quantities of a products




