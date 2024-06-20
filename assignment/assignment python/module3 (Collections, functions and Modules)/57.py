
with open("text.txt", 'r') as a:
    while True:
        data = a.readline()
        if not data:
            break
        print(data)
