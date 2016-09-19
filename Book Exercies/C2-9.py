#Made by Zachary C. on 9/11/16 last edited on 9/19/16
#1. Ask the user to enter the temperature in Celsius
#2. Save the user's input
C = float(input('Please enter the temperature in Celsius: '))

#3. Convert the input to Fahrenheit
#4. Save the converted temperature
F = (9 / 5) * C +32		#Converts the Celsius to Fahrenheit

#5. Display the converted temperature
print(C , 'degrees Celsius is' , format(F, '.1f') , 'degrees Fahrenheit')

#6. End