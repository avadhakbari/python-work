#Q.26--> Write a Python program to replace last value of tuples in a list. 
list1 = [(0,1,2,3), (4,5,7,8), (8, 9, 10,11),(12,13,14,15)]
for i in range(len(list1)):  # Loop through each tuple in the list and replace its last value with the new value
    list1[i] = list1[i][:-1] + ("avadh",)

print(list1)   # Print the updated list of tuples