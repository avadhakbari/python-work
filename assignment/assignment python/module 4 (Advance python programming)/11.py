#11. Write a Python program to write a list to a file. 

def list_write(a):
    with open("text.txt", 'w') as f:
        for i in a:
            f.write(i)


a = ['avadh', 'akbari']
list_write(a)