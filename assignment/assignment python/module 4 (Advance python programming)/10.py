#10. Write a Python program to count the frequency of words in a file. 

from collections import Counter

with open("text.txt") as f:
    a = Counter(f.read().split())

print(a)