x = "x"

def get(x, rank):
    while type(x) != float:
        try:
            print("Input", rank, "number:")
            x = float(input())
        except ValueError:
            print("Input must be a number.")
    return x
            
a = get(x, "first")
b = get(x, "second")
c = get(x, "third")

d = (a + b + c)/3
print("")
print("The average of these numbers is:", d)