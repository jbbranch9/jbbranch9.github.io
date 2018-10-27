def get(x, prompt):
    while type(x) != float:
        try:
            x = float(input(prompt))
        except ValueError:
            print("Input must be a number.")
    return x

x = "x"

odo_2 = get(x, "What is your current odometer reading?")
odo_1 = get(x, "What was your previous odometer reading?")
gal = get(x, "How much gas did it take to fill the tank?")

mileage = (odo_2 - odo_1)/gal

print("")
print("Your gas mileage for this trip was:", mileage, "mpg.")
