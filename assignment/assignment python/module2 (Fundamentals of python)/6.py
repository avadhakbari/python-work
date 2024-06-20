num1 = int(input("enter 1st number :"))
num2 = int(input("enter 2nd number :"))

temp = num1
num1 = num2
num2 = temp

print("num1 = ",num1)
print("num2 = ",num2)

# ------------------------

num1 = int(input("enter 1st number :"))
num2 = int(input("enter 2nd number :"))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1- num2

print("num1 = ",num1)
print("num2 = ",num2)