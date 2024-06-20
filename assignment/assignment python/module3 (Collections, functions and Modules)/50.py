def perfect_number(n):
    sum = 0

    for i in range(1,n):
        if n%i == 0:
            print(i)
            sum +=i
        else:
            pass

    if sum == n:
        print(n, "number is a perfect number..")
    else:
        print(n,"number is not perfect number....")

num = int(input("enter number :"))
perfect_number(num)