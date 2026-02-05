#!/usr/bin/env python3
#its a calc

a = float(input("Put in first number to add:"))
operator = input("Do an operator for the two:")
b = float(input("Now put the second!!!1!1!:"))

if operator == "+":
	result = a + b
elif operator == "-":
	result = a - b
elif operator == "*":
	result = a * b
elif operator == "/":
	result = a / b
else:
	result = "Sorry, we think you put in a wrong operator. Operators are: + is add, - is subtract, * is multiple, and / is divide."

print(result)
