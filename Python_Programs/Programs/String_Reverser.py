print("Enter a string:") #input the string
string = input()

length = len(string) #define length
z = length #z is location of last character
revstring = "!" #define reversed string using a dummy character

while z > 0:
    z = (z-1) #increment the loop
    last = string[z] #create a substring from the last character
    revstring = (revstring+last) #add substring to end of reversed string

revstring = (revstring[1:(length+1)]) #remove dummy character
print(revstring)
wait = input()