def replace(string):
    a = string.find('not')
    b = string.find('poor')
    
    if a != -1 :
        return string[:a] + 'good ' + string[a + 4:]
    elif b != -1:
        return string[:b] + 'good ' + string[b + 4:]
    else:
        return string

str= str(input("enter sentence :"))
print(replace(str))
