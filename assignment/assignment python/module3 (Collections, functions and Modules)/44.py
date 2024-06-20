# dic = {'1' : ['a', 'b'], '2' : ['c','d']}

# list1 = list(dic.values())
# total = list1 * list1

# print(total)


def generate_combinations(data, current_combination='', current_key=0):
    if current_key == len(data):
        print(current_combination)
        return

    for letter in data[str(current_key+1)]:
        generate_combinations(data, current_combination + letter, current_key + 1)

# Sample data
sample_data = {'1': ['a','b'], '2': ['c','d']}

# Generate and display combinations
generate_combinations(sample_data)
