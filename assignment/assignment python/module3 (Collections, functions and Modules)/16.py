#Q.16--> Write a Python program to check whether a list contains a sub list.
#list=[10,['chirag',2.33],[3.33,5,6],['python',"5 :hallo"]]
list1=[]   # stroge input list value
n=int(input("Enter total element :"))
for i in range(n): # loop in range n input number
    list1.append(input("value of list=")) # input value to append list1
print("orignal list=",list1)  
for i in list1:
    if len(list1) > 1: # list1 in length greter then 1
        print("sublist is present in list")
        break  # stop
    else:
        print("sub list is present not in list")