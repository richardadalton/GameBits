from random import choice

word = choice(["MONOPOLY", "FRUIT", "AUTOMOBILE", "SPORT"])
unguessed = set(word)
lives = 5

while unguessed and (lives > 0):
    print "You have {0} lives left.".format(lives)

    word_clue = ' '.join(['*' if c in unguessed else c for c in word])
    print "The word is: {0}".format(word_clue)

    guess = raw_input("Guess a letter: ")

    if guess in unguessed:
        unguessed.remove(guess)
    else:
        lives -= 1

if not unguessed:
    print "You got it, the word was {0}".format(word)
else:
    print "You didn't get it, the word was {0}".format(word)

