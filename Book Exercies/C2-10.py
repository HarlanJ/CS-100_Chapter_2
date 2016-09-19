#Made by Zachary C. on 9/11/16 last edited on 9/19/16
#1. Ask the user how many cookies to make
#2. Save the number of cookies
cookies = int(input('How many cookies would you like to make? '))

#3. Calculate the amount of each ingredient needed
#4. Save the number of each ingredient needed
percent_48 = cookies / 48
sugar = percent_48 * 1.5
butter = percent_48 * 1
flour = percent_48 * 2.75

#5. Displays the number of each ingredient needed
print('To make' , cookies , 'cookies, you will need: ' , format(sugar, '.2f') , 'cups of sugar,' , \
format(butter, '.2f') , 'cups of butter, and' , format(flour, '.2f') , 'cups of flour.')

#6. End