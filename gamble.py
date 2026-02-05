import random
import time
a = 100
bet = 0
amountmonths = 0
print("Use the ? command for info and commands")
while True:
 print("")
 cmd = input("Enter command here: ")
 if cmd == "?":
  print("")
  print("About:")
  print("ver 1.0")
  print("Made by zach, currently only colorless roulette, and number only lol")
  print("")
  print("Help:")
  print("bet = command lets you bet")
  print("balance = lets you check your balance")
  print("quit = command exits the game.")
  print("reset = resets chips back to $100")
  print("cashout = shows how many months of discord nitro pro you could buy with your money.")
 elif cmd == "bet":
  bet = int(next(i for i in iter(lambda: input("Enter number: "), '') if i.isdigit()))
  if a >= bet:
   if bet > 0:
    randomroll = random.randint(1, 2)
    if randomroll == 1:
     print("You got it!")
     a += bet
    else:
     print("You need to stop gambling.")
     a -= bet
   else:
     print("you cant bet 0 twin")
  elif a == 0:
   print("Sorry, you don't appear to have ANY chips. Use the reset command to reset back to $100") 
  else:
   print("Yeah sorry dude you don't have that many chips")
   print("")
 elif cmd == "balance":
  print("")
  print(f"${a}")
 elif cmd == "quit":
  print("exiting")
  break
 elif cmd == "reset":
  a = 100
  print("Reset succesful")
 elif cmd == "moneymoney":
  a += 1000
  print("Cheat code activated, +1000 money!!!!!!!")
 elif cmd == "cashout":
  amountmonths = a / 10
  print(f"You could afford {amountmonths} months of discord nitro pro!")
 else:
  print("")
  print("man that aint no command try again")
