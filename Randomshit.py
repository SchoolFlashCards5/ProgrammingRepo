#Sets up needed imports
import random
import time

#Gets variables for usage
a = random.randint(1, 100)
b = 0 

#Makes it so it counts when a line is printed and also counts up a, resuling in a finishing num.
while a < 100:
	print(random.choice(["Fuck you bitchy boy","Hi there!!!","YKW? I just might crash the terminal if i want.","Ok diddyblud","\033[31m Look at me im mildly rare\033[0m"]))
	time.sleep(0.05)
	b += 1
	a += 1
	print("")

#Prints end text and line number
print("Finding out finished!")
print("This is the amount of lines you got: (all are between 1-100)")
print(b)
