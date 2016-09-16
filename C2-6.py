#Made by Zachary C. on 9/11/16 last edited on 9/16/16
subtotal = float(input('Please enter the subtotal: $'))		#Asks the user to input the subtotal of their purchased items

#Calculates the county, state, and total tax, and the total cost
tax_county = subtotal * 0.025
tax_state = subtotal * 0.05
tax_total = tax_state + tax_county
total = subtotal + tax_total

#Prints the county, state, and total tax, and the total cost
print('\nThe county sales tax is: $' , format(tax_county, '.2f') , '\nThe State sales tax is: $' , format(tax_state, '.2f') , \
'\nThe total sales tax is: $' , format(tax_total, '.2f') , '\nThe total cost is: $' , format(total, '.2f') , sep='')