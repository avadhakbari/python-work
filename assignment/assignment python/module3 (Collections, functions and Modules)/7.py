list1 = [1,10,25,25,10,9,33,25,60]

li = []

for i in list1:
    if i not in li:
        li.append(i)

print(list1)
print(li)