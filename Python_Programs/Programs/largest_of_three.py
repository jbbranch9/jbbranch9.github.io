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
        
list = sorted([a, b, c])
print("The largest of these numbers is:", list[2])