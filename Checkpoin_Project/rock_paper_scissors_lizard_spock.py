
# Rock, Paper, Scissors, Lizard, Spock game
# The extended version of the game includes Lizard and Spock

rock = 1
paper = 2
scissors = 3
lizard = 4
spock = 5

import random

user_choice = int(input('Pick a number (1 for Rock, 2 for Paper, 3 for Scissors, 4 for Lizard, 5 for Spock): '))

print('You chose:' + str(user_choice))

cpu_choice = random.randint(1, 5)
print('CPU chose: ' + str(cpu_choice))

if user_choice < 1 or user_choice > 5:
    print('ERROR! Invalid input. Please choose a number between 1 and 5.')
else:
    if user_choice == cpu_choice:
        print('It is a tie!')
    elif (user_choice == rock and (cpu_choice == scissors or cpu_choice == lizard)) or \
     (user_choice == paper and (cpu_choice == rock or cpu_choice == spock)) or \
     (user_choice == scissors and (cpu_choice == paper or cpu_choice == lizard)) or \
     (user_choice == lizard and (cpu_choice == spock or cpu_choice == paper)) or \
     (user_choice == spock and (cpu_choice == scissors or cpu_choice == rock)):
        print('The player won!🏆')
    else:
        print('The CPU won!💻')
