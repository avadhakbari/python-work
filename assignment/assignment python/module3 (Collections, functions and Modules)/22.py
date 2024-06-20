tuple = (1,2,3,4,5,6,7,8,9,10)

print(tuple)

el = int(input("enter element :"))


find_element = el

if find_element in tuple:
    print("element exist in tuple")
else:
    print("element not exist in tuple")