def unzip_tuples(tuples):
    unzipped_lists = list(zip(*tuples))
    return unzipped_lists

tuples_list = [(1, 'a'), (2, 'b'), (3, 'c')]
unzipped = unzip_tuples(tuples_list)
print("Unzipped lists:", unzipped)
