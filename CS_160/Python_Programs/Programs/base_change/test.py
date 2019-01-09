def trim_binary(binary_integer):
    binary_integer = str(binary_integer)
    while binary_integer[0] == "0":
        binary_integer = binary_integer[1:]
        print(binary_integer)
    return int(binary_integer)
        
x = trim_binary("0000001100010")

print(x, type(x))