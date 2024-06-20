#8. Write a python program to find the longest words. 

long_word = ''

with open("text.txt", 'r') as f:
    for line in f:
        words = line.split()
        for word in words:
            if len(word) >len(long_word):
                long_word = word
    
print(long_word)