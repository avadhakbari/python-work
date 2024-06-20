dic ={'a' :10, 'b' :20, 'c':30, 'd':40, 'e':50}

ent_key = input("enter key for cheking :")

if ent_key in dic.keys():
    print(f"{ent_key} key is present in the dictionary....")
else:
    print(f"{ent_key} key is not present in the dictionary.....")