#Task
# Write a program for the Sorting Hat from Hogwarts

gryffindor = 0
slytherin = 0
huffelpuff = 0
ravenclaw = 0

print('Q1) Do you like Dawn or Dusk?')
print('1) Dawn')
print('2) Dusk')

answer = int (input('Enter your answer (1-2): '))

if answer == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif answer == 2:
  slytherin = slytherin + 1
  huffelpuff = huffelpuff + 1
else:
  print('Wrong input')

print('Q2) When I`m dead, I want people to remember me as: ')
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print('4) The Bold')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  huffelpuff = huffelpuff + 2
elif answer == 2:
  slytherin = slytherin + 2
elif answer == 3:
  ravenclaw = ravenclaw + 2
elif answer == 4:
  gryffindor = gryffindor + 2
else:
  print('Wrong input')

print('Q3) Which kind of instrument most pleases your ear?')
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  slytherin = slytherin + 4 
elif answer == 2:
  huffelpuff = huffelpuff + 4
elif answer == 3:
  ravenclaw = ravenclaw + 4
elif answer == 4:
  gryffindor = gryffindor + 4
else:
  print('Wrong input')

print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Huffelpuff: ", huffelpuff)
print("Slytherin: ", slytherin)

# Bonus round

if gryffindor >= ravenclaw and gryffindor >= huffelpuff and gryffindor >= slytherin:
  print('🦁 Gryffindor!')
elif ravenclaw >= gryffindor and ravenclaw >= huffelpuff and ravenclaw >= slytherin:
  print('🦅 Ravenclaw!')
elif huffelpuff >= gryffindor and huffelpuff >= ravenclaw and huffelpuff >= slytherin:
  print('🦡 Huffelpuff!')
elif slytherin >= gryffindor and slytherin >= ravenclaw and slytherin >= huffelpuff:
  print('🐍 Slytherin!')
  
# I am slytherin 🐍🫣
