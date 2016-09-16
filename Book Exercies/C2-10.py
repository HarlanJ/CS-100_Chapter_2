#Made by Zachary C. on 9/11/16 last edited on 9/16/16
cookies = int(input('How many cookies would you like to make? '))		#Asks the user to input the number of cookies they want to make

#Calculates the ammount of each ingredient needed
percent_48 = cookies / 48
sugar = percent_48 * 1.5
butter = percent_48 * 1
flour = percent_48 * 2.75

#Displays the ammount of each ingredient needed
print('To make' , cookies , 'cookies, you will need: ' , format(sugar, '.2f') , 'cups of sugar,' , \
format(butter, '.2f') , 'cups of butter, and' , format(flour, '.2f') , 'cups of flour.')