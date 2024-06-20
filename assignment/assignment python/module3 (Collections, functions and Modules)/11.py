def unique_elements(input_list):
    unique_set = set()

    for item in input_list:
        unique_set.add(item)

    unique_list = list(unique_set)
    
    return unique_list

input_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(input_list)
print("Original list:", input_list)
print("List with unique elements:", result)
