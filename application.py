"""Welcome to game guess the number"""
import random

print """
|   __|  |  |   __|   __|   __|  |  _  |  |   | |  |  |     | __  |   __| __  |
|  |  |  |  |   __|__   |__   |  |     |  | | | |  |  | | | | __ -|   __|    -|
|_____|_____|_____|_____|_____|  |__|__|  |_|___|_____|_|_|_|_____|_____|__|__|

############################################################################
#hello this is a game that tries to guess a number that is randomly created.#
#                                                                           #
#1) enter the number that you think of 1 to 20.                             #
#                                                                           #
#2) you only have 4 turns.                                                  #
#                                                                           #
#3) despuues Asher will tell you that if your                               #
#numbers is very large or small q try it buelvas.                           #
#                                                                           #
#4) after the 4 turns will ask if you want to leave or continue playing,    #
#and is to keep playing, 'No' to exit the game.                             #
#############################################################################"""                                                                        

PLAY = True
while PLAY == True:

   INPUT = random.randrange(1, 21)
   print INPUT
   TURN = 0
 
   while  TURN <= 3:
       print "This is your turn "+str(TURN +1)
       TURN = TURN + 1
       GENERATE = 0

       while GENERATE < 1 or GENERATE >20:
           GENERATE = (raw_input("insert a number in range 1 to 20: "))#in this part of the code number is entered , that user guess the random number
           try:
               GENERATE = int(GENERATE)
           except ValueError:
               pass
               #print "insert a number"
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
   while (GUESS != "y" and GUESS != "n") and (GUESS != "Y" and GUESS != "N"):
       GUESS = raw_input("Do you want to play again? (y/n:) ")
   if GUESS == "y" or GUESS == "Y" :
       PLAY = True
   elif GUESS == "n" or GUESS == "N" :
       PLAY = False #in this we use a while to prompt the user if he wants to play or quit the game