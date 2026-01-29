#!/usr/bin/env python3
"""
Hey! This is my shitty little program.
I made it with my crappy python knowledge, and  it doesn't exactly have the best of use cases.
I hope whoever decides to use it (stupidly) has fun with it.
Made with 0.00000000058 love from,
Zach.
"""

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
