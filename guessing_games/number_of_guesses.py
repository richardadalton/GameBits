from random import randint

number_of_guesses = 1
number = randint(1,100)
guess = input("I'm thinking of a number from 1 to 100, try to guess it: ")

while guess != number:
    if guess < number:
        guess = input("Too low, guess again: ")
    else:
        guess = input("Too high, guess again: ")
    number_of_guesses += 1

if number_of_guesses == 1:
    print "You got it in 1 guess"
else:
    print "You got it in {0} guesses".format(number_of_guesses)