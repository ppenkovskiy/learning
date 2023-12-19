from collections import defaultdict

with open('6_input.txt', 'r') as file:
    n = int(file.readline())
    l = [i.split(' ') for i in file.readlines()]

l.sort(key=lambda x: x[-2])
print(*l, sep='\n')