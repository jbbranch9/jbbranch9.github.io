print("Enter a string:") #input the string
string = input()

length = len(string) #define length
z = length #z is location of last character
revstring = "" #define reversed string

while z > 0:
    z = (z-1) #increment the loop
    last = string[z] #create a substring from the last character
    revstring = (revstring+last) #add substring to end of reversed string

print(revstring)
wait = input() #wait after program ends