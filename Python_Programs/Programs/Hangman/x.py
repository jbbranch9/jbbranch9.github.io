w = "white"
b = "black"

w_list = []
b_list = []

print(w,b)
print(w_list,b_list)


for x in w:
    w_list.append(x)

for x in b:
    b_list.append(x)

for x in range(len(w_list)):
    w_list[x] = b_list[x]

print(w_list,b_list)
