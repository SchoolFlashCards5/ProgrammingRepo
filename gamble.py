
import random
import time

a = 100
bet = 0

print("Use the ? command for info and commands")

while True:
 print("")
 cmd = input("Enter command here: ")
 if cmd == "printe":
  printe = input("Enter text to essentially just echo: ")
  print("")
  print(printe)
  print("")
 elif cmd == "?":
  print("About:")
  print("ver 1.0")
  print("Made by zach, currently only colorless roulette, and number only lol")
  print("")
  print("Help:")
  print("the bet command lets you bet, balance lets you check your balance, and the quit command exits the game.")
 elif cmd == "bet":
  bet = int(next(i for i in iter(lambda: input("Enter number: "), '') if i.isdigit()))
  if a >= bet:
   randomroll = random.randint(1, 2)
   if randomroll == 1:
    print("You got it!")
    a += bet
   else:
    print("You need to stop gambling.")
    a -= bet
  elif a == 0:
   print("Sorry, you dont have ANY chips. Use the quit command to exit the game, then restart the program to reset back to 100.") 
  else:
   print("Yeah sorry dude you don't have that many chips")
   print("")
 elif cmd == "balance":
  print("")
  print(a)
 elif cmd == "quit":
  break
 else:
  print("")
  print("man that aint no command try again")
