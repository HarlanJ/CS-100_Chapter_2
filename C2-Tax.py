subtotal = float(input('Please enter the subtotal: '))
tax_state = subtotal * 0.05
tax_county = subtotal * 0.025
tax_total = tax_state + tax_county
total = subtotal + tax_total

print('The subtotal is: $' , format(subtotal, '.2f') , '\nThe state sales tax is: $' , \
format(tax_state, '.2f') , '\nThe county sales tax is: $' , format(tax_county, '.2f') , \
'\nThe total sales tax is: $' , format(tax_total, '.2f') , '\nThe total cost is: $' , \
format(total, '.2f') , sep='')