"""Welcome to game guess the number"""
import random


PLAY = True
while PLAY == True:
    INPUT = random.randrange(1, 21)
    print INPUT
    TURN = 1
    while  TURN <= 4:
        TURN = TURN + 1
        GENERATE = int(raw_input("insert a number in range 1 to 20: "))
        if GENERATE < INPUT:
            print"the number is too low, try again please"
        elif GENERATE > INPUT:
            print"the number is too high, try again please"
        elif GENERATE == INPUT:
            print "YOU WIN"
            TURN = 5
        if TURN == 5:
            print "GAME OVER"

    GUESS = ""
    while GUESS != "y" and GUESS != "Y" and GUESS != "Yes" and GUESS != "YES" and GUESS != "n" and GUESS != "NO" and GUESS != "N"and GUESS != "no"and GUESS != "No" :
        GUESS = raw_input("Do you want to play again? (y/n:) ")
    if GUESS == "y" or GUESS == "yes" or GUESS == "YES" or GUESS == "Yes" or GUESS == "Y":
        PLAY = True
    elif GUESS == "n" or GUESS == "no" or GUESS == "NO" or GUESS == "N" or GUESS == "No":
        PLAY = False
