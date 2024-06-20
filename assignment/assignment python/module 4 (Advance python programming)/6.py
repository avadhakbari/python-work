#6. Write a Python program to read a file line by line and store it into a list

list1 = []
with open("text.txt" , 'r') as f:
   for line in f:
      list1.append(line)
print(list1)