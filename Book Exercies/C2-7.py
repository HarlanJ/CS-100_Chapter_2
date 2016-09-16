#Made by Zachary C. on 9/11/16 last edited on 9/16/16
#Asks the user to input the total miles traveled as well as the total gallons of gas used
miles = float(input('Please enter the miles driven: '))
gallons = float(input('Please enter the gallons used: '))

#Calculates and prints the mpg
print('\nThe MPG is: ' , format(miles / gallons, '.3f') , sep='')