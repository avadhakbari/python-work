def add_ing(string):
    if len(string) < 3:
        return string
    elif string[-3:] == 'ing':
        return string + 'ly'
    else:
        return string + 'ing'
    
a = str(input("enter string :"))
    
print(add_ing(a))
    