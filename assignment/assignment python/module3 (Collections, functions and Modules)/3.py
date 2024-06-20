#Q.3--> differentiate between append() ans extend() methods?
#    -> append :
#        append() add an item to the end of a list.
list=[1,3.33,"avadh"]
list.append("3:" "python")  # append list of last
print("append method use list :",list)

#--------------------------------------------------------------------

#    -> extend :
#        insert() inserts and item in a specified position in the list.

list1=[1,3.33,"avadh"]
list2=[10,20,30]
list1.extend(list2)   # list2 in extend list1
print("extend method use list :",list1)
  
list1=[1,5,3,21]
list1.insert(2,"Django")
print("insert method use list :",list1)