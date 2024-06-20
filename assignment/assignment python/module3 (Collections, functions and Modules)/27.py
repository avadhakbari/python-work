def find_repeated_items(tuple_data):
    repeated_items = []
    for item in tuple_data:
        if tuple_data.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items

my_tuple = (1, 2, 3, 4, 2, 5, 2, 6, 7, 7)
repeated_items = find_repeated_items(my_tuple)
print("Repeated items in the tuple:", repeated_items)
