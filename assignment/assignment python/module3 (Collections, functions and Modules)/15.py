def unique_value(input_list):
    unique_set = set()

    for i in input_list:
        unique_set.add(i)

        unique_list = list(unique_set)

    return unique_list

input_list = [1,2,2,3,4,5,5,8,10]

new = unique_value(input_list)

print("old list :", input_list)
print("new list :",new)