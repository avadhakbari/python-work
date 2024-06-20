def longest(a,b,c):
    if(len(a)>len(b) and len(a)>len(c)):
        print("length :",len(a),"= ",a)
    elif(len(b)>len(c)):
        print("length :",len(b),"=",b)
    else:
        print("lenght :",len(c), "=",c)


word1 = str(input("ente 1st word :"))
word2 = str(input("ente 2nd word :"))
word3 = str(input("ente 3rd word :"))

longest(word1, word2, word3)