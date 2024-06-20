'''Q.2-> how will you remove last object from a list?
      suppose list1 is [2,33,222,14 and 25],what is list[-1]?
ans : Using del
      The del operator deletes the element at the specified index location from the list.
      To delete the last element, we can use the negative index -1.
      The use of the negative index allows us to delete the last element, even without calculating the length of the list.''' 
        
#Ex:     
list= [2,33,222,14,25]
list=list[:-1]   # remove last object 

print("Updated list:" ,list)
    