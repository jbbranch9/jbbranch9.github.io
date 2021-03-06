import math

#this function prompts for input while ensuring the returned value is a number
def get_float(prompt):
    x = "x"
    while type(x) != float:
        try:
            x = float(input(prompt))
        except ValueError:
            print("")
            print("Error: Input must be a number.")
            print("")
    return x

#this function prompts for input while ensuring the returned value is an integer greater than zero
def get_int(prompt):
    x = "x"
    while type(x) != int or x <= 0:
        try:
            x = int(input(prompt))
        except ValueError:
            print("")
            print("Error: Input must be an integer.")
            print("")
        if type(x) == int and x <= 0:
            print("")
            print("Error: Input must be greater than zero.")
            print("")
    return x

#prompt for variables
pv = get_float("What is the amount of the loan?\n(in dollars and cents, written as a decimal)\n")
r = .01 * get_float("What is the interest rate of the loan?\n(written as a percentage, not a decimal)\n")
n = get_int("What is the term of the loan?\n(in months, written as a whole number)\n")

p = (r * pv)/(1 - math.pow((1 + r), -n))

print("Your monthly payment will be: $", str(round(p, 2)))
input()