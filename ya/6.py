with open('6_input.txt', 'r') as file:
    n = int(file.readline())
    l = [i.split(' ') for i in file if i[-1] != 'B' and i[-2:] != 'B\n']
    l = [[int(item) if index < 4 else item for index, item in enumerate(sublist)] for sublist in l]
    # print(l)

rockets_id = sorted(set(int(i[-2]) for i in l))

res = []
for r_id in rockets_id:
    res_r_id = 0

    for i in range(len(l)):
        if r_id == l[i][-2]:
            if l[i][-1][0] == 'A':
                res_r_id -= l[i][0] * 24 * 60 + l[i][1] * 60 + l[i][2]
            elif l[i][-1][0] == 'C' or l[i][-1][0] == 'S':
                res_r_id += l[i][0] * 24 * 60 + l[i][1] * 60 + l[i][2]

    res.append(res_r_id)

print(*res, sep=' ')
