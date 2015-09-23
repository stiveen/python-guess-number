"""welcome to game guess the number"""
import random #Random number generation

INGRESAR = random.randrange(1, 21) #The game most generate random number from 1 to 20
print INGRESAR #print the number

GENERATE = int(raw_input("insert a number in range 1 to 20: "))

if GENERATE < INGRESAR:  #if you insert a number that its higher that the generated number then i will recived the mesage you guess to high pleas try again
    print"the number is too high, try again please"
elif GENERATE > INGRESAR: # if you insert a number that is lower that the generated number then i will recived the mesage you guess to lo please try again.
    print"the number is too low, try again please"
elif GENERATE == INGRESAR: #if you guess the number the game will give me the mesage "You Win"
    print "YOU WIN" #here print mesage to win
