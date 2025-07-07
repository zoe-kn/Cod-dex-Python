#Task:
#Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral. First, create a ph variable and ask the user for a value between 0 and 14.
#Write an if, elif, else statement that:
#If ph is greater than 7, output "Basic".
#If ph is less than 7, output "Acidic".
#Else, output "Neutral".


#== equal to
#!= not equal to
#> greater than
#< less than
#>= greater than or equal to
#<= less than or equal to

ph = int(input('Enter a ph level (0-14): '))

if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acidic')
else:
  print('Neutral')
