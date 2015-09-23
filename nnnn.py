import random 

number=random.randrange(1, 20)
print number

ing = int(raw_input("insert a number in range 1 to 20: "))

if ing < number:
   print "the number is too small, try again please" 
elif ing > number:
    print "the number is too big, try again please"
elif ing == number:
	print "YOU WIN"	