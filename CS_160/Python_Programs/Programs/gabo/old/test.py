list1 = [30, 21, 40, 5, 19, 40]

print(max(list1))


for i in range(len(list1)):
    if list1[i] == max(list1):
        max_list = i
        
print(max_list)