with open('input.txt', 'r') as file:
    first_line = file.readline()
    a, b = [int(i) for i in first_line.split()]

with open('output.txt', 'w') as file:
    file.write(str(a + b))
