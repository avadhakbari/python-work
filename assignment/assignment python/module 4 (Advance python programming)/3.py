#3. Write a Python program to append text to a file and display the text.

with open("text.txt", 'a') as f:
    f.write("Hello Avadh")
    

with open("text.txt", 'r') as f:
    data = f.read()
    print(data)