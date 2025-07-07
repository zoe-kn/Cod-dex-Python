#Task
#Create a 99_bottles.py program and use a for loop and a range() function to print out all the verses of "99 Bottles of Beer."


for x in range(99, 0, -1): 
  print(f'{x} bottles of beer on the wall')
  print(f'{x} bottles of beer')
  print('Take one down, pass it around')
  print(f'{x - 1} bottles of beer on the wall')
