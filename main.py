# Math is a library that has some useful scientific functions like sin() and sqrt() (square root)
import math

# Here we go

# If you have not learned what input is, it is a function that allows the user to type in stuff and set it to a variable
# The parameter it takes is a string to prompt the user with
# It returns a string so you have to make sure to convert it to an float with float()
a = float(input("Enter side 'a' here: "))
b = float(input("Enter side 'b' here: "))

# ** is an operator that squares a number
csquared = (a**2 + b**2)

# Take the square root of the number
c = math.sqrt(csquared)

# print the answer
print(c)
