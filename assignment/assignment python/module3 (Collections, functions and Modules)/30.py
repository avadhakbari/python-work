def list_to_dict(list_of_tuples):
    dictionary = {}
    for key, value in list_of_tuples:
        dictionary.setdefault(key, []).append(value)
    return dictionary

list_of_tuples = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
result_dict = list_to_dict(list_of_tuples)
print(result_dict)
