#Michael Esposito
#Computer Network Defense
#CSCI 6542
#1/26/17
#Powerball_generator.

import random

while True:
	print "Official (but fruitless) Powerball number generator"
	numTries = raw_input("How many sets of numbers? ")
	try:
		numTries = int(numTries)
	except ValueError:
		print "Invalid Input, prease try again"
		continue
	for x in range(0, numTries):
		#print "Your numbers:  ", random.randint(1,53), " ",random.randint(1,53), " ", random.randint(1,53), " ",random.randint(1,53), " ", random.randint(0,53), "     Powerball: ", random.randint(1,42) 
		print "Your numbers: {:2d} {:2d} {:2d} {:2d} {:2d}     Powerball: {:2d}".format(random.randint(1,53), random.randint(1,53), random.randint(1,53), random.randint(1,53), random.randint(1,53), random.randint(1,42))
	break	