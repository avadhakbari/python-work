#9. Write a Python program to count the number of lines in a text file.

count =0

with open("text.txt", 'r') as f:
    for line in f:
        count += 1

print(count)