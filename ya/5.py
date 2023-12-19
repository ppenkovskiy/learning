with open('5_input.txt', 'r') as file:
    N = int(file.readline())
    l = [i.rstrip('\n').split(',') for i in file.readlines()]
    print(l)

v_symbols = []
for i in range(N):
    v_symbols.append(len(set(l[i][0]+l[i][1]+l[i][2])))
print(v_symbols)

day_month = []
for i in range(N):
    day_month.append((int(l[i][3])+int(l[i][4]))*64)
print(day_month)

alphabet_dict = {'a': 1,
                 'b': 2,
                 'c': 3,
                 'd': 4,
                 'e': 5,
                 'f': 6,
                 'g': 7,
                 'h': 8,
                 'i': 9,
                 'j': 10,
                 'k': 11,
                 'l': 12,
                 'm': 13,
                 'n': 14,
                 'o': 15,
                 'p': 16,
                 'q': 17,
                 'r': 18,
                 's': 19,
                 't': 20,
                 'u': 21,
                 'v': 22,
                 'w': 23,
                 'x': 24,
                 'y': 25,
                 'z': 26}

first_letter = []
for i in range(N):
    letter = l[i][0][0].lower()
    first_letter.append(alphabet_dict[letter]*256)
print(first_letter)

res = []
for i in range(N):
    res.append(v_symbols[i] +day_month[i] )