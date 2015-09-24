"""Welcome to game guess the number"""
import random


PLAY = True
while PLAY == True:
    INPUT = random.randrange(1, 21)
    print INPUT
    TURN = 0
    while  TURN <= 3:
        print "This is your turn "+str(TURN +1)
        TURN = TURN + 1
        GENERATE = int(raw_input("insert a number in range 1 to 20: "))#in this part of the code number is entered , that user guess the random number
        if GENERATE < INPUT:#if you insert a number greater or less than the number generated then I recivire retry message
            print"the number is too low, try again please"
        elif GENERATE > INPUT:
            print"the number is too high, try again please"
        elif GENERATE == INPUT:
            print "YOU WIN"
            TURN = 4
        if TURN == 4:
            print "GAME OVER"

    GUESS = ""
    while GUESS != "y" and GUESS != "Y" and GUESS != "Yes" and GUESS != "YES" and GUESS != "n" and GUESS != "NO" and GUESS != "N"and GUESS != "no"and GUESS != "No" :
        GUESS = raw_input("Do you want to play again? (y/n:) ")
    if GUESS == "y" or GUESS == "yes" or GUESS == "YES" or GUESS == "Yes" or GUESS == "Y":
        PLAY = True
    elif GUESS == "n" or GUESS == "no" or GUESS == "NO" or GUESS == "N" or GUESS == "No":
        PLAY = False #in this we use a while to prompt the user if he wants to play or quit the game