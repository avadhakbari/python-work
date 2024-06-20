def pelindrom(st):
    string = st

    rev_str = string[::-1]
    print(rev_str)

    if rev_str == string:
        print(string, "string is pelindrom ")
    else:
        print(string, "string is not pelindrom")

st = str(input("enter string :"))
pelindrom(st)