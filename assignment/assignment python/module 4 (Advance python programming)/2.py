#2. Write a Python program to read an entire text file.

with open("text.txt", 'r') as f:
    data = f.read()

    print(data)