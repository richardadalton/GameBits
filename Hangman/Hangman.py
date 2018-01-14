from random import choice

with open("/usr/share/dict/words") as f:
    words = list(set([word.lower() for word in f.read().split('\n') if len(word) > 3]))


word = choice(words)
unguessed = set(word)
lives = 5

while unguessed and (lives > 0):
    print("You have {0} lives left.".format(lives))

    word_clue = ' '.join(['*' if c in unguessed else c for c in word])
    print("The word is: {0}".format(word_clue))

    guess = input("Guess a letter: ")

    if guess in unguessed:
        unguessed.remove(guess)
    else:
        lives -= 1

if not unguessed:
    print("You got it, the word was {0}".format(word))
else:
    print("You didn't get it, the word was {0}".format(word))

