def reverse_multiple(string):
    if len(string) %4 == 0:
        return string[::-1]
    else:
        return string
    
a = str(input("enter string :"))
print(reverse_multiple(a))