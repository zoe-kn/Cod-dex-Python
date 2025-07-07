#Task 
#First, introduce a variable called tries at the top and give it a value of 0.
#Then, add a second condition with the tries variable to the while loop using a relational operator.

tries = 0
guess = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))
  tries = tries + 1

if guess != 6:
  print('you ran out of tries')
else:
  print("You got it!")
