#Task
#Create a fizz_buzz.py program that outputs numbers from 1 to 100.
#For multiples of 3, print "Fizz" instead of the number.
#For multiples of 5, print "Buzz" instead of the number.
#Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".

for i in range(1, 101):            # Because it need to start from 1 not 0
  if i % 3 == 0 and i % 5 == 0:    #If a number is a multiple of 3, its num % 3 == 0, because the remainder is 0
    print('FizzBuzz')              #'FizzBuzz' needs to come first because it captures numbers that are multiples of both 3 and 5
  elif i % 3 == 0:
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  else:
    print(i)
