# Aqui escribe tu codigo

print "Hello World"
import random 

number=random.randrange(1, 20)

ing = raw_input("insert a number in range 1 to 20")

if number < ing :
	print "the number is too small, please try again" 
elif number >ing:
	print "the number is too big, please try again"
