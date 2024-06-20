# Write a Python program to find the highest 3 values in a dictionary 

dic = {'a' : 1, 'b' : 10, 'c' : 15, 'd' : 5, 'e' : 24}

list = []

for i in dic.values():
    list.append(i)

list.sort(reverse=True)
print(list[0:3])
