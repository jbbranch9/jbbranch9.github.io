def get(prompt):
    x = "x"
    while type(x) != float:
        try:
            print("Input", prompt, "number:")
            x = float(input())
        except ValueError:
            print("")
            print("Error: Input must be a number.")
            print("")
    return x
            
a = get("first")
b = get("second")
c = get("third")

d = (a + b + c)/3
print("The average of these numbers is:", d)
input()