import random #Random number generation
number=random.randrange(1, 20)#The game most generate random number from 1 to 20
print number #print the number genetared

ing = int(raw_input("insert a number in range 1 to 20: "))

if ing > number: #if you insert a number that its higher that the generated number then i will recived the mesage you guess to high pleas try again
   print "the number is too high, try again please" 
elif ing < number: # if you insert a number that is lower that the generated number then i will recived the mesage you guess to lo please try again.
    print "the number is too low, try again please"
elif ing == number: #if you guess the number the game will give me the mesage "You Win"
	print "YOU WIN"