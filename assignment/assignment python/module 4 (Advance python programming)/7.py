#7. Write a Python program to read a file line by line store it into a variable. 

a = ""

with open("text.txt", 'r') as f:
    data = f.readlines()
    a = data

print(a)