#Made by Zachary C. on 9/11/16 last edited on 9/16/16
#Asks the user to input the number of male and female students in their class
students_male = int(input('How many male students are in your class? '))
students_female = int(input('How many female students are in your class? '))

#Calculates the percentages of male and female students in the class
students_total = students_male + students_female
percent_male = (students_male / students_total) * 100
percent_femaile = (students_female / students_total) * 100

#Displays the percentage of male and female students in the class
print('Your class is ' , format(percent_male, '.0f') , '% male, and ' , format(percent_femaile, '.0f') , '% female.' , sep='')