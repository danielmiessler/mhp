# MHP -- The Monty Hall Problem
# This program will test the 50/50 vs. 1/3-2/3 options
# (for 3 doors) in the Monty Hall Problem.

import random
import sys

stayandwin = 0
switchandwin = 0

# Make sure an argument is given when the program is run

try:
	nop = len(sys.argv)
except:
        sys.exit("Please enter the number of times you want to run the test.")

if nop !=2:
        sys.exit("Usage: mhp <number of times to run the test>")

# Take in the number of times to run the test

try:
        iterations = int(sys.argv[1])
except:
        sys.exit("Usage: mhp <number of times to run the test>")

for i in xrange(iterations):
	# Determine where the car is
	car = random.randint(1,3)

	# Determine the user's choice
	choice = random.randint(1,3)
 	
	# Increment winner	
	if car == choice:
		stayandwin += 1
	else:
		switchandwin += 1

# Print results

print "If you STAY you win " + str(stayandwin) + " times."
print "If you SWITCH you win " + str(switchandwin) + " times."
