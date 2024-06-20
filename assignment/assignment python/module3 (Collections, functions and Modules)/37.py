dic = {'name' : 'avadh', 'age' : 18, 5: 'avadh'}

list = list(dic.keys())

for i in list:
    if type(i) == int:
        print("integer key in dictionary is :",i)
    else:
        continue