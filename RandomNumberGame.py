import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20. And you have 6 chances to guess it right.')

# Giving 6 chances to guess
for guessesTaken in range(1, 7):        #here is a smart way of using range() function
   print('Take a guess.')
   guess = int(input())
   if guess < secretNumber:
     print('Your guess is too low.')
   elif guess > secretNumber:
     print('Your guess is too high.')
   else:
     break 
      
# Once 6 chances are over
if guess == secretNumber:
   print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')    #when the previous loop breaks, the final value is stored in guessTaken variable
else:
   print('Nope. The number I was thinking of was ' + str(secretNumber))
