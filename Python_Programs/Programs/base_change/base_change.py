import math

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear') #import screen clearing function from os
    
def string_to_list(string):
    list = []
    for i in string:
        list.append(i)
    return list

def get_base(prompt, in_base, out_base): #prompts user for a base number system, either for input or output
    number_base = ""
    while type(number_base) == str:
        try:
            screen_refresh(in_base, out_base)
            print("Select", prompt, "type:\n1) binary\n2) octal\n3) decimal\n4) hexadecimal\n")
            number_base = int(input())
        except ValueError:
            input("\nError: Please type the number (1-4) only.\nPress enter to return.\n")
        if type(number_base) == int and (number_base > 4 or number_base < 1):
            number_base = ""
            input("\nError: Please type the number (1-4) only.\nPress enter to return.\n")
    return number_base

def input_output_bases(): #uses get_base() to choose input and output bases, and ensures they are discrete
    in_base = 0
    out_base = 0
    while in_base == 0:
        screen_refresh(in_base, out_base)
        in_base = get_base("input", in_base, out_base)
        screen_refresh(in_base, out_base)        
        out_base = get_base("output", in_base, out_base)
        if out_base == in_base:
            cls()
            print("Error: Output base must be different from input base.\n")
            in_base = 0
            out_base = 0
            input()
    return in_base, out_base

def test_invalid_character(in_base, integer):
    integer_list = string_to_list(str(integer))
    invalid_character = False
    if in_base == 1:
        character_list = ["0", "1"]
    if in_base == 2:
        character_list = ["0", "1", "2", "3", "4", "5", "6", "7"]
    if in_base == 3:
        character_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if in_base == 4:
        character_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    for i in range(len(integer_list)):
        if str(integer_list[i]) not in character_list:
            invalid_character = True
    return invalid_character
          
def get_integer(in_base, out_base):
    valid = False
    while valid == False:
        screen_refresh(in_base, out_base)
        integer = input("Input a positive integer: \n\n ")
        if test_invalid_character(in_base, integer):
            input("\nError: Invalid character for input base.\nPress enter to return.\n")  
        else:
            valid = True
        if in_base != 4:
            integer = int(integer)
    return integer

def string_reverse(string):
    z = len(string) #z is location of last character
    revstring = "" #define reversed string
    while z > 0:
        z = (z-1) 
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
    
def binary_to_decimal(integer):
    bin_str = string_to_list(str(integer))
    decimal_number = int(0)
    #this builds a decimal as a sum of powers of 2
    for i in range(len(bin_str)):
        index = len(bin_str) - i - 1
        decimal_number = decimal_number + (int(bin_str[index]) * 2**i)
    return decimal_number

def format_binary(string, iteration):
    #adds "0" to left end of string until string length is evenly divisible by the "iteration" value
    while len(string) % iteration != 0:
        string = "0" + string
    return string

def binary_to_octal(integer):
    octal_number = ""
    formatted_binary = format_binary(str(integer), 3)
    #this divides the binary into blocks of 3 digits, and converts them to single octal digits
    for i in range(int(len(formatted_binary)/3)):
        octal_number = octal_number + str(binary_to_decimal(formatted_binary[3*i:(3*i)+3]))
    return octal_number

def octal_to_binary(integer):
    integer = str(integer)
    binary_number = ""
    #this iterates through the octal integer, replacing each digit with its 3-digit binary equivalent
    for i in range(len(integer)):
        binary_number = binary_number + ["000", "001", "010", "011", "100", "101", "110", "111"][int((integer)[i])]
    return binary_number

def binary_to_hexadecimal(integer):
    formatted_binary = format_binary(str(integer), 4)
    hexadecimal_list = []
    for i in range(int(len(formatted_binary)/4)):
        hexadecimal_list.append(binary_to_decimal(formatted_binary[4*i:(4*i)+4]))
    hexadecimal_number = ""
    for i in range(len(hexadecimal_list)):
        hexadecimal_number = hexadecimal_number + ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"][hexadecimal_list[i]]
    return hexadecimal_number

def hexadecimal_list_to_decimal(hexadecimal_list):
    for i in range(len(hexadecimal_list)):
        if hexadecimal_list[i] == "a":
            hexadecimal_list[i] = 10
        if hexadecimal_list[i] == "b":
            hexadecimal_list[i] = 11
        if hexadecimal_list[i] == "c":
            hexadecimal_list[i] = 12
        if hexadecimal_list[i] == "d":
            hexadecimal_list[i] = 13
        if hexadecimal_list[i] == "e":
            hexadecimal_list[i] = 14
        if hexadecimal_list[i] == "f":
            hexadecimal_list[i] = 15
    return hexadecimal_list

def hexadecimal_to_binary(integer):
    hexadecimal_list = string_to_list(str(integer))
    decimal_list = hexadecimal_list_to_decimal(hexadecimal_list)
    binary_number = ""
    for i in range(len(decimal_list)):
        binary_number = binary_number + format_binary(decimal_to_binary(int(decimal_list[i])), 4)
    return binary_number

def trim_binary(binary_integer):
    binary_integer = str(binary_integer)
    while binary_integer[0] == "0":
        binary_integer = binary_integer[1:]
    return int(binary_integer)

def get_binary_integer(in_base, integer):
    if in_base == 1:
        binary_integer = integer
    if in_base == 2:
        binary_integer = octal_to_binary(integer)
    if in_base == 3:
        binary_integer = decimal_to_binary(integer)
    if in_base == 4:
        binary_integer = hexadecimal_to_binary(integer)
    return binary_integer

def get_output_number(out_base, binary_integer):
    if out_base == 1:
        output_number = trim_binary(str(binary_integer))
    if out_base == 2:
        output_number = binary_to_octal(binary_integer)
    if out_base == 3:
        output_number = binary_to_decimal(binary_integer)
    if out_base == 4:
        output_number = binary_to_hexadecimal(binary_integer)
    return output_number

def base_number_to_text(base):
    if base == 1:
        text = "binary"
    elif base == 2:
        text = "octal"
    elif base == 3:
        text = "decimal"
    elif base == 4:
        text = "hexadecimal"
    else:
        text = ""
    return text

def screen_refresh(in_base, out_base):
    in_base_text = base_number_to_text(in_base)
    out_base_text = base_number_to_text(out_base)
    cls()
    print("==========base_change.py==========\n")
    print("From: ", in_base_text, "To: ", out_base_text, "\n")

def main():
    in_base, out_base = input_output_bases()
    integer = get_integer(in_base, out_base)
    binary_integer = get_binary_integer(in_base, integer)
    print("\nin ", base_number_to_text(out_base), "=\n\n", get_output_number(out_base, binary_integer))

while True:
    main()
    input()