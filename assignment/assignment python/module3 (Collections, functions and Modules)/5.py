#Q.5--> How will you compare two list?
#list1=['ch','chirag','c','chi','chir','chira']
#list2=['chirag','chi','c','ch','chira','chir']

list1=[]    # storge in list1 of input value
n=int(input("Enter element of list1:"))
for i in range(n):   # loop in range input num
    list1.append(int(input("value="))) # input value
print("list1 is=",list1) 

list2=[]  # storge in list2 of input value
n=int(input("Enter element of list2 :"))
for i in range(n): # loop in range input num
    list2.append(int(input("value="))) # input value
print("list2 is=",list2)

list1.sort() # sort method use Ascending value 
print("Ascending list1=",list1)
list2.sort()
print("Ascending list1=",list2)
print("\n")
if (list1 == list2): # check list1 & list2 are eqal
    print("[The list1 and list2 are equal]")
else:
    print("[The list1 and list2 are  not equal]")