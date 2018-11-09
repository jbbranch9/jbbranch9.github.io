import math

def get_base(prompt): #prompts user for a base number system, either for input or output
    number_base = ""
    while type(number_base) == str:
        try:
            print("Select", prompt, "type:\n1) binary\n2) octal\n3) decimal\n4) hexadecimal\n")
            number_base = int(input())
        except ValueError:
            print("\nPlease type the number (1-4) only.\n")
        if type(number_base) == int and (number_base > 4 or number_base < 1):
            print("\nPlease type the number (1-4) only.\n")
            number_base = ""
    return number_base

def input_output_bases(): #uses get_base() to choose input and output bases, and ensures they are discrete
    in_base = 0
    while in_base == 0:
        in_base = get_base("input")
        out_base = get_base("output")
        if out_base == in_base:
            print("Output base must be different from input base.\n")
            in_base = 0
    return in_base, out_base

input_output_bases()

def get_integer():
    negative = False
    integer = ""
    while type(integer) != int:
        try:
           integer = int(input("Pick an integer: \n"))
        except ValueError:
            print("Input must be an integer.\n")
    """
    Some of the modules in this program don't work
    for negative integer inputs. However, since
    multiplication is transitive, I can divide out a
    -1 as needed, set the variable "negative" to "True",
    and multiply the converted digits by -1
    at the end of the program.    
    """
    if integer < 0:
        negative = True
        integer = -integer
    return integer, negative

def string_reverse(string):
    z = len(string) #z is location of last character
    revstring = "" #define reversed string
    while z > 0:
        z = (z-1) #increment the loop
        last = string[z] #create a substring from the last character
        revstring = (revstring+last) #add substring to end of reversed string
    return revstring

def decimal_to_binary(integer):
    bin_str = []
    """
    This while loop works by:
    A) dividing the integer by 2,
    B) placing the remainder in the "1's place,"
    C) dividing the dividend by 2,
    D) placing the remainder in the "2's place,"
    repeat C) and D) for the 4's, 8's, 16's etc.
    until dividend >= 1    
    """
    while integer >= 1:
        dividend = math.floor(integer/2)
        remainder = integer % 2
        bin_str.append(str(remainder))
        integer = dividend
    """
    The algorithm above actually produces the reverse of
    the binary number (with the 1's place on the left).
    The function call below reverses it to proper format.
    """
    bin_str = string_reverse(bin_str) 
    return bin_str
    
def main():
    integer, negative = get_integer()
    output_number = decimal_to_binary(integer)
    if negative:
        print("-", output_number)
    else:
        print(output_number)
        
main()
input()
