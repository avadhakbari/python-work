#5. Write a Python program to read last n lines of a file

def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()
        last_n_lines = lines[-n:]
        return last_n_lines


filename = 'text.txt'
n = 3


last_lines = read_last_n_lines(filename, n)
print(last_lines)
