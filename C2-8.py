#Made by Zachary C. on 9/16/16 last edited on 9/16/16
cost = float(input('How much did the meal cost? $'))		#Asks the user to input the cost of the food

#Calculates the tip, tax, and total
tip = cost * 0.18
tax = cost * 0.07
total = cost + tip + tax

#Displays the tip, tax, and total
print('\nYour tip should be: $' , format(tip , '.2f') , '\nThe tax is: $' , format(tax , '.2f') , '\nThe total cost is: $' , format(total , '.2f') , sep='')