while True:
    eq = input("Enter your equation here: ")
    try:
        ans = eval(eq)
        print(ans)
        print("")
    except ZeroDivisionError:
        print("Sorry mate, you cant divide by zero.")
        print("")
    except Exception:
        print("That ain't a valid equation twin")
        print("")
