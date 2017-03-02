from random import randint

best_score = None
best_score_name = None

game_over = False

while not game_over:
    number_of_guesses = 1
    number = randint(1, 100)
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

    if best_score is None:
        best_score = number_of_guesses
        best_score_name = raw_input("New best score, enter your name: ")
    else:
        if number_of_guesses < best_score:
            best_score = number_of_guesses
            best_score_name = raw_input("New best score, enter your name: ")

    print "The best score is {0} by {1}".format(best_score, best_score_name)

    play_again = raw_input("Would you like to play again? (Y/N)? ").upper()[:1]
    game_over = play_again != 'Y'

