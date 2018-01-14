from random import randint

heaps = {'A': randint(3, 9),
         'B': randint(3, 9),
         'C': randint(3, 9)}


def Display_Heaps():
    print ("The heaps are:")
    for heap, count in sorted(heaps.items()):
        print ("In heap {0}, there are {1}".format(heap, count))

def Get_Move_From_Player():
    while True:
        Display_Heaps()
        heap = input("It's {0}'s turn. Which heap do you want to take from? : ".format(players[player]))
        if not heap in heaps:
            print ("There is no heap called {0}".format(heap))
        else:
            how_many = int(input("How many would you like to take from heap {0}? : ".format(heap)))
            if how_many > heaps[heap]:
                print ("There aren't {0} pieces in heap {1}".format(how_many, heap))
            else:
                return heap, how_many

player1 = input("Enter Player One's Name: ")
player2 = input("Enter Player Two's Name: ")
players = [player1, player2]


game_over=False
player = 0

while not game_over:
    heap, how_many = Get_Move_From_Player()
    heaps[heap] -= how_many

    if heaps[heap] == 0:
        del heaps[heap]

    if not heaps:
        break

    player += 1
    player = player % 2


print ("{0} has taken the last piece and is the winner".format(players[player]))