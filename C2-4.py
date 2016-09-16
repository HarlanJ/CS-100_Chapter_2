#Made by Zachary C. on 9/11/16 last edited on 9/16/16
#Asks the user to input the cost of the items 
item_1 = float(input('Please input the cost of the first item: '))
item_2 = float(input('Please input the cost of the second item: '))
item_3 = float(input('Please input the cost of the third item: '))
item_4 = float(input('Please input the cost of the fourth item: '))
item_5 = float(input('Please input the cost of the fifth item: '))

#Calculates the subtotal, tax, and total
subtotal = item_1 + item_2 + item_3 + item_4 + item_5
tax = subtotal * 0.07
total = subtotal + tax

#Displays the subtotal, tax, and total
print('\nThe subtotal is: $' , format(subtotal, '.2f') , '\nThe tax is: $' , \
format(tax, '.2f') , '\nThe total is: $' , format(total, '.2f') , sep='')