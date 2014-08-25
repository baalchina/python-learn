#!/usr/bin/env python

f = file('products.txt')
products = []
prices = []
for line in f.readlines():
        new_line = line.split()
        products.append(new_line[0])
        prices.append(int(new_line[1]))

#print products
#print prices

salary = int(raw_input("Pleas input your salary:"))

while True:
        print "Welcome, things you can buy as below:"
        for p in products:
                p_index = products.index(p)
                p_price = prices[p_index]
                print p,p_index,p_price
        choice = raw_input('Please input what you want to buy:')
        f_choice = choice.strip()
        if f_choice in products:
                print "Yes"
                f_index = products.index(f_choice)
                f_price = prices[f_index]
                if salary >= f_price:
                        print "Added %s to shopping list!" %f_choice
        else:
                print "Not in the list, try again!"