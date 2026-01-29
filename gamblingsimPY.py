import random
import sys
balance = 100
b = 0
cmd = 0
ran = 0
print("Use the about command to view about, and  the ? command for help.")
while True:
    cmd = input("Enter cmd: ")
    if cmd == "balance":
        print(balance)
        print("")
    elif cmd == "?":
        print("bet command lets you bet, balance command lets you view balance, and quit command closes out the game.?")
        print("")
    elif cmd == "bet": 
        betam = int(input("How much to bet: "))
        if betam <= balance:
            if  betam > 0:
                b = betam
                ran = random.randint(1, 2)
                if ran == 1:
                    balance += b
                    print("You winned")
                else:
                    balance -= b
                    print("You loses")
                print("")
            else:
                print("You cannot bet 0 or below.")
        else:
            print("You dont got allat many chips twin")
    elif cmd == "about":
        print("This is ver ex1.0")
        print("This is a placeholder ver made in school")
        print("Main ver is ver1.1")
        print("Will be moving over soon")
        print("")
    elif cmd == "quit":
        print("Exiting...")
        sys.exit(0)
    elif cmd == "reset":
        balance = 100
    elif cmd == "e":
        balance += 100
    elif cmd == "ext":
        balance += 500
    elif cmd == "un":
        balance += 1000
    else:
        print("Thats not a command bum bum")
        print("")
