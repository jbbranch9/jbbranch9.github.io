import math

def get_integer():
    negative = False
    integer = ""
    while type(integer) != int:
        try:
           integer = int(input("Pick an integer: \n"))
        except ValueError:
            print("Input must be an integer.\n")
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
    while integer >= 1:
        dividend = math.floor(integer/2)
        remainder = integer % 2
        #print(integer, dividend, remainder)
        bin_str.append(str(remainder))
        integer = dividend
    bin_str = string_reverse(bin_str)
    return bin_str
    
def main():
    integer, negative = get_integer()
    binary = decimal_to_binary(integer)
    if negative:
        print("-", binary)
    else:
        print(binary)
        
main()
input()

    