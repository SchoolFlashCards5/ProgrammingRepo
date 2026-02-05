
#!/usr/bin/env python3
#its a calc
print("")
print("Operators are: + is add, - is subtract, * is multiple, and / is divide.")
print("You can also use = to determine if a number is equal (they always are or arent because we only have straight nums rn)")
print("You can also use > or < to determine if two numbers are more or less.")
print("")
a = float(input("Put in first number to add: "))
operator = input("Do an operator for the two: ")
b = float(input("Now put the second!!!1!1!: "))

if operator == "+":
	result = a + b
elif operator == "-":
	result = a - b
elif operator == "*":
	result = a * b
elif operator == "/":
	result = a / b
elif operator == "=":
    if a == b:
        result = f"True, {a} = {b}"
    else:
        resutl = f"False, {a} doesnt = {b}"
elif operator == "<":
    if a < b:
        result = f"True, {a} < {b}"
    else:
        result = f"False, {a} > {b}"
elif operator == ">":
    if a > b:
        result = f"True, {a} > {b}"
    else:
        result = f"False, {a} < {b}"
else:
	result = "Sorry, we think you put in a wrong operator. Operators are: + is add, - is subtract, * is multiple, and / is divide."

print(result)
