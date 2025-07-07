# Rock Paper Scissors Game

rock = 1
paper = 2
scissors = 3

import random

user_choice = int(input('Pick a number (1 for Rock, 2 for Paper, 3 for Scissors): '))

print('You chose:' + str(user_choice))

cpu_choice = random.randint(1, 3)
print('CPU chose: ' + str(cpu_choice))

if user_choice == cpu_choice:
    print('It is a tie!')
elif (user_choice == rock and cpu_choice == scissors) or (user_choice == paper and cpu_choice == rock) or (user_choice == scissors and cpu_choice == paper):
    print('The player won!🏆')
elif (cpu_choice == rock and user_choice == scissors) or (cpu_choice == paper and user_choice == rock) or (cpu_choice == scissors and user_choice == paper):
    print('The CPU won!💻')
else:
    print('ERROR! Invalid input.')