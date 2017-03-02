from random import random, randint, choice

def make_expression():
    if random() < 0.1:
        left = "({0})".format(make_expression())
    else:
        left = randint(1, 9)

    if random() < 0.1:
        right = "({0})".format(make_expression())
    else:
        right = randint(1, 9)

    op = choice(['+', '-', '*'])
    return "{0} {1} {2}".format(left, op, right)

while True:
    expression = make_expression()
    answer = str(eval(expression))
    guess = raw_input("What is {0}: ".format(expression))

    if guess == answer:
        print "That's right"
    else:
        print "That's wrong, it was {0}".format(answer)