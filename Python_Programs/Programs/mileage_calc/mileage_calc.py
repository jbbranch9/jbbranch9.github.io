def get(prompt):
    x = "x"
    while type(x) != float:
        try:
            x = float(input(prompt))
        except ValueError:
            print("")
            print("Error: Input must be a number.")
            print("")
    return x

odo_2 = get("What is your current odometer reading?\n")
odo_1 = get("What was your previous odometer reading?\n")
gal = get("How much gas did it take to fill the tank?\n")

mileage = (odo_2 - odo_1)/gal

print("Your gas mileage for this trip was:", mileage, "mpg.")
input()