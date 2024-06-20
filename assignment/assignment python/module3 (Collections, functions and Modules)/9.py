def common_member(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
    
    return bool(set1.intersection(set2))

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print(common_member(list1, list2))  
