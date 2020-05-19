import random
import pyinputplus as pyip

guess_count = 0;
player_name = pyip.inputStr(prompt='Hello! What is your name: ')
s = 'Hello %s Enter the upper range of the number: ' % player_name
max_num = pyip.inputInt(prompt=s)
number = random.randint(1, max_num)
print('Well %s, I am thinking of a number between 1 and %s' % (player_name, max_num))

for guess_taken in range(6):
    guess = pyip.inputInt(prompt='Take a Guess: ')
    if guess < number:
        print('Your guess is too low :(')

    if guess > number:
        print('Your guess is too high :(')

    if guess == number:
        break

if guess == number:
    print('Good Job %s! You guessed my number in %s guesses' % (player_name, guess_taken+1))

if guess != number:
    print('Nope the number I was thinking about was %s.'% number)