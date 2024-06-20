#4. Write a Python program to read first n lines of a file. 

with open("text.txt", 'r') as f:
    data = f.readline()
    print(data)
