list_of_tuples = [(1, 2), (), (3, 4), (), (5, 6), ()]

cleaned_list = []
for tup in list_of_tuples:
    if tup:
        print(tup)
        cleaned_list.append(tup)

print("List after removing empty tuples:", cleaned_list)
