def middle_string(a,b):
    midd = len(a)//2
    return a[:midd] + b + a[midd:]


str1 = str(input("enter 1st string :"))
str2 = str(input("enter 2nd string :"))

print(middle_string(str1,str2))