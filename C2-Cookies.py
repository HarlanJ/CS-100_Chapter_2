cookies = int(input('How many cookies would you like to make? '))

percent_48 = cookies / 48
sugar = percent_48 * 1.5
butter = percent_48 * 1
flour = percent_48 * 2.75

print('To make' , cookies , 'cookies, you will need: ' , format(sugar, '.2f') , 'cups of sugar,' , \
format(butter, '.2f') , 'cups of butter, and' , format(flour, '.2f') , 'cups of flour.')