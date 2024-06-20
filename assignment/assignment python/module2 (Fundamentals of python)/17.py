
a = str(input("enter 1st string :"))
b = str(input("enter 2nd string :"))

print("before swipe :", a ,b)

a = a[1] + a[0]+ a[2:]
b = b[1] + b[0]+ b[2:]

print("after swipe :",a , b )