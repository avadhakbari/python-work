dic1 = {'a' : 100, 'b' : 200, 'c' : 300}
dic2 = {'a' : 200, 'b' : 300, 'c' : 400}
dic3 = {}
list = []

for key ,val in dic1.items():
    for key1, val1 in dic2.items():
        if key == key1:
            total = val + val1
    list.append(total)

