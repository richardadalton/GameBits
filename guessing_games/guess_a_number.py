from random import randint

number = randint(1,100)
guess = input("I'm thinking of a number from 1 to 100, try to guess it: ")

while guess != number:
    if guess < number:
        guess = input("Too low, guess again: ")
    else:
        guess = input("Too high, guess again: ")

print "You Got It"