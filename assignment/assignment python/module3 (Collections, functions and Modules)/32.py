#Write a Python script to sort (ascending and descending) a dictionary by value

dic = {'a' : 5, 'b' : 4, 'c' : 2, 'd' :1, 'e' : 3}
list1 = list(dic.values())
list1.sort()

print("assending order")
for i in list1:
    for key, val in dic.items():
        if val == i:
            print(key,val,end=",")


list2 = list(dic.values())
list2.sort(reverse=True)
print("\ndesending order")

for i in list2:
    for key,val in dic.items():
        if val == i:
            print(key,val, end=",")