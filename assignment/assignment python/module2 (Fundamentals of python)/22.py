def first_last(string):
    if len(string) < 2 :
        return 'empty set'
    else:
        return string[:2] + string[-2:]
    
a = str(input("etner string :"))

print(first_last(a))