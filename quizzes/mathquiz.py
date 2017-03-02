from random import randint, choice

while True:
    firstNum = randint(1, 9)
    secondNum = randint(1, 9)
    op = choice(['+', '-', '*', '/'])

    expression = "{0} {1} {2}".format(firstNum, op, secondNum)
    answer = str(eval(expression))
    guess = raw_input("What is {0}: ".format(expression))

    if guess == answer:
        print "That's right"
    else:
        print "That's wrong, it was {0}".format(answer)